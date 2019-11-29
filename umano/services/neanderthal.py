from dataclasses import dataclass
from datetime import datetime
from optparse import make_option
import os
import random
import sys
import time
from threading import Thread
from dacite import from_dict, Optional

import cv2
import numpy as np
from pythonosc.udp_client import SimpleUDPClient

from umano.onehand import midi
from umano.onehand.models import HandFeature, Metronome, Bjorklund
from umano.onehand.utils import frequency_to_note, rescale_frame
from umano.onehand.osc import send_cave_to_vuo
from umano.hal.data import find
from umano.services.base import DataFetcher
from umano import settings


def stop_note(note, port, delta):
    time.sleep(delta)
    client = SimpleUDPClient(settings.ONEHAND_LIVE_HOST, port)
    client.send_message("/midi/note", note.to_off_list())
    return


@dataclass(repr=True)
class Position:
    x: int
    y: int


@dataclass(repr=True)
class ImageSize:
    w: int
    h: int


@dataclass(repr=True)
class CaveHand:
    uid: str
    join_date: datetime
    audio: str
    hand_image: str
    features_image: str
    delay: float
    duration: float
    new_member: bool
    position: Optional[Position]
    pixel_position: Optional[Position]
    size: Optional[ImageSize]
    rotation: Optional[float]
    features: HandFeature

    def roi(self):
        return Position(self.pixel_position.x - 50 + self.size.w // 2,
                        self.pixel_position.y - 50 + self.size.h // 2), Position(
            self.pixel_position.x + 50 + self.size.w // 2, self.pixel_position.y + 50 + self.size.h // 2)


@dataclass(repr=True)
class Note:
    note: midi.MidiNote
    timestamp: float
    duration: float


class Pattern(object):

    def __init__(self, notes) -> None:
        super().__init__()
        self.notes = notes

    def play(self, ip=settings.ONEHAND_LIVE_HOST, base_port=settings.ONEHAND_LIVE_PORT):
        clients = {
            0: SimpleUDPClient(address=ip, port=base_port),
            1: SimpleUDPClient(address=ip, port=base_port + 1),
            2: SimpleUDPClient(address=ip, port=base_port + 2),
            3: SimpleUDPClient(address=ip, port=base_port + 3),
        }

        previous_timestamp = 0

        round_robin = 0

        for note in self.notes:
            time.sleep(note.timestamp - previous_timestamp)
            previous_timestamp = note.timestamp
            clients[round_robin].send_message("/midi/note", note.note.to_list())
            Thread(target=stop_note, daemon=True, args=(note.note, base_port + round_robin, note.duration)).start()
            round_robin = (round_robin + 1) % len(clients)


class Column(object):

    def __init__(self, idx, offset, width, height, capacity, padding_x, padding_y, pixel_coordinates=True, window=None):
        super().__init__()
        self.idx = idx
        self.offset = offset
        self.width = width
        self.height = height
        self.padding_x = padding_x
        self.padding_y = padding_y
        self.capacity = capacity
        self.hands = []
        self.pixel_coordinates = pixel_coordinates
        self.aspect_ratio = None
        self.center = None

        if not self.pixel_coordinates and window is not None:
            self.center = Position(x=round(window.w / 2), y=round(window.h / 2))
            self.aspect_ratio = window.h / window.w

    def add_hand(self, hand: CaveHand, min_size: ImageSize, max_size: ImageSize):
        if self.has_capacity:
            hand.size = self.generate_size(hand, min_size, max_size)
            hand.pixel_position = self.generate_position(hand)
            hand.position = self.from_pixel_to_coordinates(hand.pixel_position)
            hand.rotation = self.generate_rotation(hand)
            self.hands.append(hand)
            if hand.new_member:
                self.capacity = 1

    @property
    def has_capacity(self):
        return len(self.hands) < self.capacity

    @staticmethod
    def generate_rotation(hand):
        return round(-5.0 - random.random() * 5.0, 2)

    @staticmethod
    def generate_size(hand: CaveHand, min_size: ImageSize, max_size: ImageSize):
        if hand.new_member:
            return max_size
        else:
            w = round(random.randrange(min_size.w, max_size.w))
            h = round(w / hand.size.w * hand.size.h)
            return ImageSize(
                w=w,
                h=h
            )

    def overlap(self, x, y):
        if x is None or y is None:
            return True

        for hand in self.hands:
            roi_min, roi_max = hand.roi()
            if roi_min.x < x < roi_max.x and roi_max.y < y < roi_min.y:
                return True

        return False

    def from_pixel_to_coordinates(self, pixel_position):
        x = round((pixel_position.x - self.center.x) / self.center.x, 2)
        y = round(self.aspect_ratio * (self.center.y - pixel_position.y) / self.center.y, 2)
        return Position(x, y)

    def generate_position(self, hand: CaveHand):
        if hand.new_member:
            x = self.offset + self.width // 2
            y = self.height // 2
        else:
            x = None
            y = None
            while self.overlap(x, y):
                x = round(
                    self.offset + self.padding_x + hand.size.w / 2 + random.randint(0, self.width - 2 * self.padding_x))
                y = round(self.padding_y + hand.size.h / 2 + random.randint(0,
                                                                            self.height - 2 * self.padding_y - hand.size.h // 2))
        return Position(x=x, y=y)

    def empty(self):
        self.hands = []


class Neanderthal(DataFetcher):
    option_list = DataFetcher.option_list + [
        make_option(
            '--debug',
            dest='DEBUG',
            action="store_true",
            default=False,
            help='Show debug image'
        )
    ]

    def __init__(self, data_class="OneHandFeatures", timeout=10, n_columns=8, column_width=None, column_height=920,
                 column_offset=None, column_padding_x=100, column_padding_y=100, capacity=15, n_hands=30, min_size=None,
                 max_size=None, debug=False,
                 pixel_coordinates=False, window_width=4096, window_height=1080) -> None:
        super().__init__(data_class, timeout)
        self.name = "Neanderthal"
        self.description = "Cave orchestra director"
        self.new_member_column = 4
        self.orchestra_members = 20
        self.columns = []
        self.hands = []
        self.n_hands = n_hands

        self.audio_directory = os.path.join(settings.UMANO_SHARE_ROOT, "onehand/audio")
        self.image_directory = os.path.join(settings.UMANO_SHARE_ROOT, "onehand/pictures")

        self.min_size = min_size
        self.max_size = max_size

        self.client = SimpleUDPClient(settings.ONEHAND_VUO_HOST, settings.ONEHAND_VUO_PORT)
        self.client_max = SimpleUDPClient(settings.ONEHAND_MAX_HOST, settings.ONEHAND_MAX_PORT)

        self.symphony = []
        self.timeout = 25
        self.duration = 0

        self.debug = debug
        self.window = ImageSize(w=window_width, h=window_height)

        if not isinstance(column_offset, list):
            column_offset = [column_offset] * n_columns

        if not isinstance(column_width, list):
            column_width = [column_width] * n_columns

        for i in range(n_columns):

            offset = column_offset[i]
            for k in range(i):
                offset += column_offset[k] + column_width[k]

            column = Column(
                idx=i + 1,
                padding_x=column_padding_x,
                padding_y=column_padding_y,
                width=column_width[i],
                height=column_height,
                offset=offset,
                capacity=isinstance(capacity, list) and capacity[i] or capacity,
                pixel_coordinates=pixel_coordinates,
                window=self.window
            )

            self.columns.append(
                column
            )

    def process_args_and_options(self, args, options):
        super().process_args_and_options(args, options)
        self.debug = options.DEBUG

    def audio_path(self, uid):
        return os.path.join(self.audio_directory, "{}{}".format(uid, settings.ONEHAND_HAND_AUDIO_EXTENSION))

    def picture_path(self, uid):
        return os.path.join(self.image_directory, "{}{}".format(uid, settings.ONEHAND_HAND_PICTURES_EXTENSION))

    def picture_features_path(self, uid):
        return os.path.join(self.image_directory, "{}_features{}".format(uid, settings.ONEHAND_HAND_PICTURES_EXTENSION))

    def compose_symphony(self):
        self.symphony = []
        metronome = Metronome(bpm=220)
        pattern = Bjorklund(steps=metronome.bars * metronome.beat_resolution, pulses=len(self.hands)).pattern
        hand = None
        idx = 0
        self.duration = 0
        while metronome.has_next():
            if metronome.counter % metronome.beat_resolution == 0 \
                    and pattern[metronome.counter // metronome.beat_resolution]:
                if hand is None:
                    hand = self.hands[idx]
                    idx = (idx + 1) % len(self.hands)
                i = random.randint(0, hand.features.features_length - 1)
                if hand.features.frequencies[i] == float('inf'):
                    continue
                duration = float(random.randint(3, 5) * 1000)
                note = Note(
                    note=midi.MidiNote(
                        note=getattr(midi, frequency_to_note(hand.features.frequencies[i])),
                        velocity=hand.features.amplitudes[i] * 127,
                        duration=duration
                    ),
                    timestamp=metronome.time,
                    duration=duration
                )
                self.duration = max([self.duration, metronome.time + duration/1000])
                self.symphony.append(note)
            metronome.tick()
        print(self.duration)

    def send_osc(self):
        if self.debug:
            frame = np.zeros(shape=[self.window.h, self.window.w, 3])

            WHITE = (255, 255, 255)
            for column in self.columns:
                print((column.offset, 0), (column.offset+column.width, column.height))
                cv2.rectangle(frame, (column.offset, 0), (column.offset+column.width, column.height), WHITE, thickness=2)
            for hand in self.hands:
                p1, p2 = hand.roi()
                cv2.rectangle(frame, (p1.x, p1.y), (p2.x, p2.y), WHITE,
                              thickness=2)
            cv2.imshow("debug", rescale_frame(frame))
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            sys.exit(0)

        else:
            self.log(msg="update cave {}".format(len(self.hands)))
            pattern = Pattern(notes=self.symphony)
            Thread(target=pattern.play, daemon=True).start()
            send_cave_to_vuo(self.hands, self.duration)

    def fetch_data(self):
        self.data = find(
            self.data_class,
            query={'hand_print': True, 'shared': True},
            sort_key="create_time",
            sort_direction=-1,
            limit=self.n_hands
        )

    def process_data(self):
        id_column = 0
        for column in self.columns:
            column.empty()

        for idx, hand_features in enumerate(self.data):
            id_column = (id_column + 1) % len(self.columns)
            if not self.columns[id_column].has_capacity:
                continue
            self.columns[id_column].add_hand(
                from_dict(
                    CaveHand,
                    data=dict(
                        uid=hand_features.uid,
                        join_date=hand_features.create_time,
                        audio=self.audio_path(hand_features.uid),
                        hand_image=self.picture_path(hand_features.uid),
                        features_image=self.picture_features_path(hand_features.uid),
                        delay=random.random() * 5.0,
                        duration=random.random() * 10.0,
                        new_member=idx == 0,
                        size=ImageSize(hand_features.width, hand_features.height),
                        features=HandFeature(hand_features.image_points)
                    )
                ),
                min_size=self.min_size,
                max_size=self.max_size
            )

        self.hands = []
        for column in self.columns:
            for hand in column.hands:
                self.hands.append(hand)

        self.compose_symphony()
        self.send_osc()
        time.sleep(self.timeout)
        sys.exit(0)


if __name__ == "__main__":
    screen_w = 4096
    screen_h = 1080
    n_columns = 8
    column_width = [
        485,
        519,
        509,
        457,
        479,
        519,
        519,
        440
    ]
    column_offset = [
        0,
        25,
        25,
        25,
        0,
        25,
        25,
        25
    ]
    service = Neanderthal(
        n_columns=n_columns,
        column_height=screen_h,
        column_offset=column_offset,
        min_size=ImageSize(250, 250),
        max_size=ImageSize(400, 400),
        n_hands=50,
        pixel_coordinates=False,
        window_height=screen_h,
        window_width=screen_w,
        column_width=column_width,
        column_padding_x=150,
        column_padding_y=100,
        capacity=10
    )

    service.run()
