import os
import platform
from optparse import make_option
import shutil

from pymongo import MongoClient
import requests

from umano.hal.data import store
from umano.hal.models import OneHandFeatures
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
        )
    ]

    def __init__(self, data_class="OneHandFeatures", timeout=10) -> None:
        super().__init__(data_class, timeout)
        self.name = "Lara Croft"
        self.description = "Search for lost hands prints an bring them to the museum"
        self.server = "http://localhost:9000"
        self.output_directory = settings.UMANO_SHARE_ROOT
        self.onehand_remote = MongoClient('mongodb://manosola:27017').umano[settings.HAL_DATA_ONEHAND_FEATURES_COLLECTION]

    def process_args_and_options(self, args, options):
        self.timeout = options.TIMEOUT
        self.server = options.SERVER
        if not os.path.exists(self.output_directory):
            os.makedirs(self.output_directory)

    def from_url_to_file(self, url, output_path):
        response = requests.get(url, stream=True)
        self.log(msg="download image from url: {} - {}".format(response.status_code, url))
        if response.status_code == 200:
            with open(output_path, 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)
            del response
            return True
        return False

    def fetch_data(self):

        # HACK! import hands from manosola
        cursor = self.onehand_remote.find({"create_time": {"$gte": self.last_update}})
        onehand_local = OneHandFeatures.get_collection()
        for data in cursor:
            if not data.get("hand_print"):
                continue
            if onehand_local.count_documents({"_id": data.get("_id")}) > 0:
                continue
            data['shared'] = False
            hand = store(data_class=OneHandFeatures, data=data, force=True)
            self.log("unburied hand {} from manosola pit".format(hand.uid))
            # break

        super().fetch_data()

    def process_data(self):
        for hand_feature in self.data:
            if not hand_feature.hand_print:
                continue
            if hand_feature.shared:
                continue
            audio_path = os.path.join(
                self.output_directory, "onehand/audio",
                "{}{}".format(hand_feature.uid, settings.ONEHAND_HAND_AUDIO_EXTENSION))
            image_path = os.path.join(
                self.output_directory, "onehand/pictures",
                "{}{}".format(hand_feature.uid, settings.ONEHAND_HAND_PICTURES_EXTENSION))
            download_ok = self.from_url_to_file(
                "{}/audio/{}".format(self.server,
                                     "{}{}".format(hand_feature.uid, settings.ONEHAND_HAND_AUDIO_EXTENSION)),
                audio_path
            )
            if not download_ok:
                continue

            download_ok = self.from_url_to_file(
                "{}/handprints/{}".format(self.server,
                                          "{}{}".format(hand_feature.uid, settings.ONEHAND_HAND_PICTURES_EXTENSION)),
                image_path
            )

            if not download_ok:
                continue

            for host in settings.UMANO_SHARE_HOSTS:
                if platform.system() == "Darwin":
                    share_in_host = "/Volumes/{}/umano-share".format(host, settings.UMANO_SHARE_ROOT)
                    if os.path.exists(share_in_host):
                        self.log("copy data to host {}".format(host))

                        if not os.path.exists(audio_path.replace(settings.UMANO_SHARE_ROOT, share_in_host)):
                            shutil.copy(audio_path, audio_path.replace(settings.UMANO_SHARE_ROOT, share_in_host))
                        if not os.path.exists(image_path.replace(settings.UMANO_SHARE_ROOT, share_in_host)):
                            shutil.copy(image_path, image_path.replace(settings.UMANO_SHARE_ROOT, share_in_host))

            hand_feature.shared = True
            hand_feature.save()


if __name__ == "__main__":
    service = LaraCroft()
    service.run()
