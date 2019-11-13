import os
import random
from dataclasses import dataclass
from datetime import datetime

from dacite import from_dict, Optional

from pythonosc.udp_client import SimpleUDPClient

from umano.onehand.osc import send_cave_to_vuo
from umano.hal.data import find
from umano.services.base import DataFetcher
from umano import settings


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
    size: Optional[ImageSize]
    rotation: Optional[float]


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
            hand.position = self.generate_position(hand)
            hand.rotation = self.generate_rotation(hand)
            self.hands.append(hand)
            if hand.new_member:
                self.capacity = 1

    @property
    def has_capacity(self):
        return len(self.hands) < self.capacity

    @staticmethod
    def generate_rotation(hand):
        # return round(-10.0 + random.random() * 25.0, 2)
        return round(-30.0 - random.random() * 25.0, 2)

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

    def generate_position(self, hand: CaveHand):
        if hand.new_member:
            x = self.offset + self.width // 2
            y = self.height // 2
        else:
            x = round(self.offset + self.padding_x + hand.size.w/2 + random.randint(0, self.width - 2 * self.padding_x))
            y = round(self.padding_y + hand.size.h/2 + random.randint(0, self.height - 2 * self.padding_y - hand.size.h // 2))

        if not self.pixel_coordinates and self.aspect_ratio is not None:
            # self.log(msg=x, y)
            x = round((x - self.center.x) / self.center.x, 2)
            y = round(self.aspect_ratio * (self.center.y - y) / self.center.y, 2)
            # self.log(msg=x, y)

        return Position(x=x, y=y)

    def empty(self):
        self.hands = []


class Neanderthal(DataFetcher):

    def __init__(self, data_class="OneHandFeatures", timeout=10, n_columns=8, column_width=500, column_height=920,
                 column_offset=200, column_padding_x=100, column_padding_y=100, capacity=15, n_hands=30, min_size=None, max_size=None,
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

        for i in range(n_columns):
            column = Column(
                idx=i + 1,
                padding_x=column_padding_x,
                padding_y=column_padding_y,
                width=isinstance(column_width, list) and column_width[i] or column_width,
                height=column_height,
                offset=(column_width + column_offset) * i,
                capacity=isinstance(capacity, list) and capacity[i] or capacity,
                pixel_coordinates=pixel_coordinates,
                window=ImageSize(w=window_width, h=window_height)
            )

            self.columns.append(
                column
            )

    def audio_path(self, uid):
        return os.path.join(self.audio_directory, "{}{}".format(uid, settings.ONEHAND_HAND_AUDIO_EXTENSION))

    def picture_path(self, uid):
        return os.path.join(self.image_directory, "{}{}".format(uid, settings.ONEHAND_HAND_PICTURES_EXTENSION))

    def picture_features_path(self, uid):
        return os.path.join(self.image_directory, "{}_features{}".format(uid, settings.ONEHAND_HAND_PICTURES_EXTENSION))

    def send_osc(self):
        hands = []
        for column in self.columns:
            for hand in column.hands:
                hands.append(hand)

        self.log(msg="update cave {}".format(len(hands)))
        send_cave_to_vuo(hands)

    def fetch_data(self):
        self.data = find(
            self.data_class,
            sort_key="create_time",
            sort_direction=-1,
            limit=self.n_hands
        )

    def process_data(self):
        id_column = 0
        for column in self.columns:
            column.empty()
        fake_data = self.data + self.data
        for idx, hand_features in enumerate(fake_data):
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
                        size=ImageSize(hand_features.width, hand_features.height)
                    )
                ),
                min_size=self.min_size,
                max_size=self.max_size
            )
        self.send_osc()


if __name__ == "__main__":
    screen_w = 4096
    screen_h = 1080
    offset = 25
    n_columns = 8
    column_width = [
        485,
        519,
        509,
        457,
        479,
        519,
        519,
        440,
    ]
    column_offset = [

    ]
    service = Neanderthal(
        n_columns=n_columns,
        column_height=screen_h,
        column_offset=offset,
        min_size=ImageSize(300, 300),
        max_size=ImageSize(500, 500),
        n_hands=30,
        pixel_coordinates=False,
        window_height=screen_h,
        window_width=screen_w,
        column_width=519,
        column_padding_x=37,
        column_padding_y=100,
        capacity=10
    )


    service.run()
