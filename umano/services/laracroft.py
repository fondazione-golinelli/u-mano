import os
from optparse import make_option
import shutil

import requests
from umano.hal.data import last
from umano.services.base import DataFetcher
from umano import settings


class LaraCroft(DataFetcher):
    option_list = DataFetcher.option_list + [
        make_option(
            '--server',
            dest='SERVER',
            type=str,
            default="http://localhost:9000",
            help='Http Server url to connect to (default "http://localhost:9000")'
        ),
        make_option(
            '--output-directory',
            dest='OUTPUT_DIRECTORY',
            type=str,
            default=settings.UMANO_SHARE_ROOT,
            help='Local directory to save images to (default to umano share {})'.format(settings.UMANO_SHARE_ROOT)
        ),
        make_option(
            '--local',
            dest='LOCAL',
            type=str,
            default=False,
            help='Read images and audio from local directory'
        ),
    ]

    def __init__(self, data_class="OneHandFeatures", timeout=10) -> None:
        super().__init__(data_class, timeout)
        self.name = "Lara Croft"
        self.description = "Search for lost hands prints an bring them to the museum"
        self.server = "http://localhost:9000"
        self.output_directory = os.path.join(os.getcwd(), "downloads")

    def process_args_and_options(self, args, options):
        self.timeout = options.TIMEOUT
        self.server = options.SERVER
        self.output_directory = options.OUTPUT_DIRECTORY
        if not os.path.exists(self.output_directory):
            os.makedirs(self.output_directory)

    @staticmethod
    def from_url_to_file(url, output_path):
        response = requests.get(url, stream=True)
        print("download image from url: {} - {}".format(response.status_code, url))
        if response.status_code == 200:
            with open(output_path, 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)
            del response

    def process_data(self):
        for hand_feature in self.data:

            self.from_url_to_file(
                "{}/audio/{}".format(self.server,
                                     "{}{}".format(hand_feature.uid, settings.ONEHAND_HAND_AUDIO_EXTENSION)),
                os.path.join(
                    self.output_directory, "onehand/audio",
                    "{}{}".format(hand_feature.uid, settings.ONEHAND_HAND_AUDIO_EXTENSION))
            )

            self.from_url_to_file(
                "{}/handprints/{}".format(self.server,
                                        "{}{}".format(hand_feature.uid, settings.ONEHAND_HAND_PICTURES_EXTENSION)),
                os.path.join(
                    self.output_directory, "onehand/pictures",
                    "{}{}".format(hand_feature.uid, settings.ONEHAND_HAND_PICTURES_EXTENSION))
            )

            self.from_url_to_file(
                "{}/handprints/{}".format(self.server,
                                        "{}_features{}".format(hand_feature.uid, settings.ONEHAND_HAND_PICTURES_EXTENSION)),
                os.path.join(
                    self.output_directory, "onehand/pictures",
                    "{}_features{}".format(hand_feature.uid, settings.ONEHAND_HAND_PICTURES_EXTENSION))
            )


if __name__ == "__main__":
    service = LaraCroft()
    service.run()
