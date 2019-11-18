import random
import uuid

from umano.onehand.durer import durerizer
from umano.onehand.utils import *


class Bjorklund():
    def __init__(self, steps: int, pulses: int):
        if pulses > steps:
            raise ValueError
        self.pattern = []
        level = 0
        counts = []
        remainders = []
        divisor = steps - pulses

        remainders.append(pulses)
        while True:
            counts.append(divisor / remainders[level])
            remainders.append(divisor % remainders[level])
            divisor = remainders[level]
            level += 1
            if remainders[level] < 2:
                break
        counts.append(divisor)

        def build(level: int):
            if level == -1:
                self.pattern.append(0)
            elif level == -2:
                self.pattern.append(1)
            else:
                # recursion
                for i in range(0, int(counts[level])):
                    build(level - 1)
                if remainders[level] != 0:
                    build(level - 2)

        build(level)
        i = self.pattern.index(1)
        self.pattern = self.pattern[i:] + self.pattern[0:i]


class Metronome(object):

    def __init__(self, bpm=120, beats=4, beat_resolution=4, bars=16):
        self.bpm = bpm
        self.counter = 0
        self.beats = beats
        self.max = bars * beat_resolution * beats
        self.beat_resolution = beat_resolution
        self.bars = bars
        self.time_division = 60 / (self.bpm * beat_resolution)

    def tick(self):
        if self.has_next():
            self.counter += 1

    def reset(self):
        self.counter = 0

    @property
    def time(self):
        return self.counter * self.time_division

    def has_next(self):
        return self.counter < self.max


class HandFeature(object):

    def __init__(self, image_points=None, reference_frequency=64, source_image=None,
                 duration=12000.0, frequency_delta=50, amplitude_decrease=0.2,
                 default_attack=2000.0, default_decay=1000.0, default_release=3000.0):
        if isinstance(image_points, list):
            self.image_points = image_points
        else:
            raise ValueError("image_points must be a list!")
        self.source_image = source_image
        self.reference_frequency = reference_frequency
        self.duration = duration
        self.frequency_delta = frequency_delta
        self.amplitude_decrease = amplitude_decrease
        self.default_attack = default_attack
        self.default_release = default_release

        self.frequencies, self.distances, self.hand_length = points_to_frequencies(image_points, reference_frequency)
        self.durer_frequencies, self.durer_distances, _ = points_to_frequencies(durerizer(self.hand_length),
                                                                                reference_frequency)
        self.amplitudes = self.ones
        self.durer_amplitudes = self.ones

        self.features_length = len(self.frequencies)
        self.beats = self.zeros
        self.attacks = [default_attack] * self.features_length
        self.decays = [default_decay] * self.features_length
        self.releases = [default_release] * self.features_length
        self.envelopes = [""] * self.features_length

        # TODO saprai sicuramente inventarti degli id più accattivanti!
        self.uid = str(uuid.uuid4())[:4]
        points_per_finger = 4

        for i in range(self.features_length):
            self.attacks[i] = self.default_attack * (i % points_per_finger + 1)
            self.releases[i] = self.default_release * (4 - (i % points_per_finger))
            self.beats[i] = self.default_attack * (i % points_per_finger) * 1000

        for i in range(self.features_length):
            self.durer_amplitudes[i] = self.amplitude_decrease
            frequency_diff = abs(self.frequencies[i] - self.durer_frequencies[i])
            if frequency_diff == float('inf'):
                continue
            if frequency_diff > self.frequency_delta:
                self.durer_amplitudes[i] = max([0.1, self.durer_amplitudes[i] - (
                        self.amplitude_decrease * frequency_diff / (self.frequency_delta * points_per_finger)
                )])
            if self.frequencies[i] > self.reference_frequency * 8:
                self.amplitudes[i] -= self.amplitude_decrease

        for i in range(self.features_length):
            self.envelopes[i] = "\"0, {amp} {att} {amp2} {dec} 0. {rel}\"".format(
                amp=self.amplitudes[i], att=self.attacks[i], amp2=self.amplitudes[i] - amplitude_decrease,
                dec=self.decays[i], rel=self.releases[i])

        self.frequencies = list(map(lambda x: round(x, 2), self.frequencies))
        self.durer_frequencies = list(map(lambda x: round(x, 2), self.durer_frequencies))
        self.amplitudes = list(map(lambda x: round(x, 2), self.amplitudes))
        self.decays = list(map(lambda x: round(x, 2), self.decays))
        self.releases = list(map(lambda x: round(x, 2), self.releases))
        self.attacks = list(map(lambda x: round(x, 2), self.attacks))

    def reverse(self):
        self.beats.reverse()
        self.releases.reverse()
        self.attacks.reverse()

    def notes(self):
        return [frequency_to_note(f) for f in self.frequencies]

    @staticmethod
    def index_to_finger(i):
        n_phalanx = 4
        if 0 <= i < 4:
            finger = "thumb"
        elif 4 <= i < 8:
            finger = "index"
        elif 8 <= i < 12:
            finger = "middle"
        elif 12 <= i < 16:
            finger = "ring"
        else:
            finger = "little"

        return finger, 1 + i % n_phalanx

    def finger_to_finger(self, start=1):
        for i in range(len(self.frequencies)):
            finger, phalanx = self.index_to_finger(i)
            data = [
                round(self.distances[i]),
                self.frequencies[i],
                self.amplitudes[i],
                round(self.durer_distances[i]),
                self.durer_frequencies[i],
                self.durer_amplitudes[i],
                self.beats[i],
                self.attacks[i],
                self.decays[i],
                self.releases[i]
            ]
            yield finger, phalanx, data

    @property
    def zeros(self):
        return [0.0] * len(self.frequencies)

    @property
    def ones(self):
        return [1.0] * len(self.frequencies)
