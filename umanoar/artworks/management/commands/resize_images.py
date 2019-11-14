import os
from PIL import Image

from django.core.management.base import BaseCommand, no_translations
from artworks.models import ArtworkQueryImageResult
from artworks.utils import IMAGE_EXTENSIONS


class Command(BaseCommand):
    help = 'Attention, to work properly make it run twice :)'

    def add_arguments(self, parser):
        parser.add_argument(
            '--width',
            action='store',
            dest="width",
            default=512,
            help='Target width',
        )
        # parser.add_argument(
        #     '--only_images',
        #     action='store_true',
        #     default=False,
        #     help='Fetch only images',
        # )
        pass

    @no_translations
    def handle(self, *args, **options):

        max_dimension = int(options.get("width"))
        for q in ArtworkQueryImageResult.objects.all():
            try:
                print("processing {}".format(q.image.name))
                if q.image.name.split(".")[-1].lower() not in IMAGE_EXTENSIONS:
                    print("delete")
                    path = q.image.path
                    q.delete()
                    os.remove(path)
                img = Image.open(q.image.path)

                if img.size[0] > max_dimension:
                    w_percent = max_dimension / float(img.size[0])
                    h_size = int(float(img.size[1]) * float(w_percent))
                    img = img.resize((max_dimension, h_size), Image.ANTIALIAS)

                elif img.size[1] > max_dimension:
                    h_percent = max_dimension / float(img.size[1])
                    w_size = int(float(img.size[0]) * float(h_percent))
                    img = img.resize((w_size, max_dimension), Image.ANTIALIAS)

                img.save(q.image.path)

            except BaseException as e:
                print("error {}".format(e))
