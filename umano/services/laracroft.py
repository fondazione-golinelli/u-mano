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
            default=os.path.join(os.getcwd(), "downloads"),
            help='Local directory to save images to (default downloads under current directory)'
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

    def process_data(self):
        for hand_feature in self.data:
            hand_picture = last("OneHandPicture", query={"touch_session_id": hand_feature.touch_session_id})
            if hand_picture is None:
                print("something bad happened!")
                continue

            url = "{}/pictures/{}".format(self.server, hand_picture.filename)
            response = requests.get(url, stream=True)
            output_path = os.path.join(self.output_directory, "{}{}".format(hand_feature.uid, settings.ONEHAND_HAND_PICTURES_EXTENSION))
            with open(output_path, 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)
            del response

            pass


if __name__ == "__main__":
    service = IndianaJones()
    service.run()
