import cv2

from django.core.management.base import BaseCommand, no_translations
from artworks.models import ArtworkQueryImageResult

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        # parser.add_argument(
        #     '--width',
        #     action='store',
        #     dest="width",
        #
        #     help='Delete existing query result',
        # )
        # parser.add_argument(
        #     '--only_images',
        #     action='store_true',
        #     default=False,
        #     help='Fetch only images',
        # )
        pass

    @no_translations
    def handle(self, *args, **options):

        max_width = 1024

        for q in ArtworkQueryImageResult.objects.all():
            try:
                print("processing {}".format(q.image.name))
                image = cv2.imread(q.image.path)

                if image.shape[0] > max_width:
                    height = round(1024 / image.shape[0] * image.shape[1])
                    image = cv2.resize(image, (max_width, height), interpolation=cv2.INTER_AREA)
                    cv2.imwrite(q.image.path, image)

                    print("\t image {} resized correctly".format(q))
            except cv2.error:
                print("error!")
                q.delete()
