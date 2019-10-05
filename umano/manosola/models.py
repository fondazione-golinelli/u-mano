from umano.manosola.durer import durerizer
from umano.manosola.utils import *


class HandFeature(object):
    
    def __init__(self, image_points=None, reference_frequency=64, source_image=None):
        if isinstance(image_points, list):
            self.image_points = image_points
        else:
            raise ValueError("image_points must be a list!")
        self.source_image = source_image
        self.reference_frequency = reference_frequency

        self.frequencies, self.distances, self.hand_length = points_to_frequencies(image_points, reference_frequency)
        self.durer_frequencies, self.durer_distances, _ = points_to_frequencies(durerizer(self.hand_length), reference_frequency)
        self.amplitudes = self.durer_amplitudes = []
        # TODO calcola le ampiezze a modo
        for f in self.frequencies:
            self.amplitudes.append(1.0)
            self.durer_amplitudes.append(1.0)

    def notes(self):
        return [frequency_to_note(f) for f in self.frequencies]

    @property
    def zeros(self):
        return [0.0] * len(self.frequencies)

    @property
    def ones(self):
        return [1.0] * len(self.frequencies)

    @staticmethod
    def get_index(a, b):
        return a > 0 and a or b

    def finger(self, a, b):
        return dict(
            f=[f for f in self.frequencies[a:b] if f]
        )

    def thumb(self):
        return self.finger(0, 4)

    def index(self):
        return self.finger(4, 8)

    def middle(self):
        return self.finger(8, 12)

    def ring(self):
        return self.finger(12, 16)

    def little(self):
        return self.finger(16, 20)

    def to_dict(self):
        return dict(
            src=self.source_image,
            frequencies=self.frequencies,
            distances=self.distances,
            fingers=dict(
                thumb=self.thumb(),
                index=self.index(),
                middle=self.middle(),
                ring=self.ring(),
                little=self.little()
            )
        )
