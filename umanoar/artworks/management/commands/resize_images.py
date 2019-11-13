import os
from PIL import Image

from django.core.management.base import BaseCommand, no_translations
from artworks.models import ArtworkQueryImageResult
from artworks.utils import IMAGE_EXTENSIONS


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument(
            '--width',
            action='store',
            dest="width",
            default=1024,
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

        max_width = int(options.get("width"))
        for q in ArtworkQueryImageResult.objects.all():
            try:
                print("processing {}".format(q.image.name))
                if q.image.name.split(".")[-1].lower() not in IMAGE_EXTENSIONS:
                    print("delete")
                    path = q.image.path
                    q.delete()
                    os.remove(path)
                img = Image.open(q.image.path)
                w_percent = (max_width / float(img.size[0]))
                h_size = int((float(img.size[1]) * float(w_percent)))
                img = img.resize((max_width, h_size), Image.ANTIALIAS)
                img.save(q.image.path)
            except BaseException as e:
                print("error {}".format(e))
