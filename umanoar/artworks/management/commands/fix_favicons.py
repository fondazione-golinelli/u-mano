import os
import shutil
import requests
from django.core.management.base import BaseCommand, CommandError, no_translations
from artworks.models import ArtworkQueryResultWebsite, ArtworkQueryTextResult

from artworks.management.commands.google_query import create_website_for_url


class Command(BaseCommand):
    help = 'Better safe than sorry'

    @no_translations
    def handle(self, *args, **options):
        for w in ArtworkQueryResultWebsite.objects.all():

            try:
                print("processing {}".format(w.domain))
                if w.favicon is not None and w.favicon.file is not None and w.favicon.file.size == 0:
                    print(w)
                    w.favicon = None
                    w.save()
                    try:
                        os.remove(w.favicon.file.name)
                    except PermissionError:
                        print("permission error, no worries")

                if w.favicon is not None and "ico" in w.favicon.file.name:
                    print("ico favicon, replacing")
                    qq = ArtworkQueryTextResult.objects.filter(website=w).first()
                    if qq is not None:
                        create_website_for_url(qq.url, force_update=True)
                    w.save()
            except (ValueError, requests.exceptions.ConnectionError):
                print("error {}".format(w))
                w.favicon = None
                w.save()
