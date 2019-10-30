from umano.onehand.durer import durerizer
from umano.onehand.utils import *


class HandFeature(object):

    def __init__(self, image_points=None, reference_frequency=64, source_image=None):
        if isinstance(image_points, list):
            self.image_points = image_points
        else:
            raise ValueError("image_points must be a list!")
        self.source_image = source_image
        self.reference_frequency = reference_frequency

        self.frequencies, self.distances, self.hand_length = points_to_frequencies(image_points, reference_frequency)
        self.durer_frequencies, self.durer_distances, _ = points_to_frequencies(durerizer(self.hand_length),
                                                                                reference_frequency)
        self.amplitudes = self.durer_amplitudes = []
        # TODO calcola le ampiezze a modo
        for f in self.frequencies:
            self.amplitudes.append(1.0)
            self.durer_amplitudes.append(1.0)

    def notes(self):
        return [frequency_to_note(f) for f in self.frequencies]

    def finger_to_finger(self, start=1):
        n_phalanx = 4
        for i in range(len(self.frequencies)):
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

            data = [
                round(self.distances[i]),
                self.frequencies[i],
                self.amplitudes[i],
                round(self.durer_distances[i]),
                self.durer_frequencies[i],
                self.durer_amplitudes[i],
                0.0  # placeholder for timing
            ]
            yield finger, start + i % n_phalanx, data

    @property
    def zeros(self):
        return [0.0] * len(self.frequencies)

    @property
    def ones(self):
        return [1.0] * len(self.frequencies)



