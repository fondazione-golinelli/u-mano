import os
import shutil
from django.core.management.base import BaseCommand, CommandError, no_translations
from artworks.models import ArtworkQueryResultWebsite


class Command(BaseCommand):
    help = 'Better safe than sorry'

    @no_translations
    def handle(self, *args, **options):
        for w in ArtworkQueryResultWebsite.objects.all():

            try:
                if w.favicon is not None and w.favicon.file is not None and w.favicon.file.size == 0:
                    print(w)
                    w.favicon = None
                    w.save()
                    try:
                        os.remove(w.favicon.file.name)
                    except PermissionError:
                        print("permission error, no worries")
            except ValueError:
                print("error {}".format(w))
                w.favicon = None
                w.save()