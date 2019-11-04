import random

from umano.onehand.durer import durerizer
from umano.onehand.utils import *


class HandFeature(object):

    def __init__(self, image_points=None, reference_frequency=64, source_image=None,
                 duration=15000.0, frequency_delta=50, amplitude_decrease=0.3,
                 default_attack=3000.0, default_release=2000.0):
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

        self.attacks = self.zeros
        self.decays = self.zeros
        self.releases = self.zeros
        self.beats = self.zeros

        features_length = len(self.frequencies)

        points_per_finger = 4
        for i in range(features_length):
            if i % points_per_finger == 0:
                self.beats[i] = 0.0
            else:
                self.beats[i] = self.distances[i-1] + self.beats[i - 1]

        for i in range(features_length):
            self.beats[i] = round(self.duration * self.beats[i] / self.hand_length)
            self.attacks[i] = round(self.duration * self.beats[i] / self.hand_length)

        for i in range(features_length):
            self.attacks[i] = self.default_attack
            self.releases[i] = self.default_release
            if self.beats[i] == 0.0:
                self.attacks[i] = self.duration / points_per_finger
                self.releases[i] = self.beats[i + 1] + self.default_release
            elif i < features_length - 1:
                self.attacks[i] = abs(self.beats[i+1] - self.beats[i])
            if i % points_per_finger == 3:
                self.attacks[i] = self.default_attack / points_per_finger
                self.releases[i] = self.default_release / points_per_finger

        for i in range(features_length):
            frequency_diff = abs(self.frequencies[i] - self.durer_frequencies[i])
            if frequency_diff == float('inf'):
                continue
            if frequency_diff > self.frequency_delta:
                self.durer_amplitudes[i] = max([0.1, self.durer_amplitudes[i] - (
                    self.amplitude_decrease * frequency_diff / (self.frequency_delta * points_per_finger)
                )])
            if self.frequencies[i] > self.reference_frequency * 8:
                self.amplitudes[i] -= self.amplitude_decrease

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

