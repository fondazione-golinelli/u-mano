import os
from io import BytesIO
from urllib.parse import urljoin, urlsplit
import uuid
import requests
from bs4 import BeautifulSoup
from googlesearch import search
from google_images_search import GoogleImagesSearch
import wikipedia

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError, no_translations
from django.core.files import File
from django.core.exceptions import MultipleObjectsReturned

from artworks.models import Artwork, ArtworkQueryTextResult, ArtworkQueryImageResult, ArtworkQueryResultWebsite
from artworks.utils import domain_from_url, base_url, IMAGE_EXTENSIONS


def save_image_from_url(model, image_field, image_url, image_filename):
    r = requests.get(image_url)
    if r.status_code == 200:
        fp = BytesIO()
        fp.write(r.content)
        getattr(model, image_field).save(image_filename, File(fp))
        return True
    else:
        return False


def create_website_for_url(url, force_update=False):
    scheme, domain = domain_from_url(url)
    try:
        website, created = ArtworkQueryResultWebsite.objects.get_or_create(domain=domain)
    except MultipleObjectsReturned:
        website = ArtworkQueryResultWebsite.objects.filter(domain=domain).first()
        created = False
    if created or force_update:
        icon_url = urljoin("{}://{}".format(scheme, domain), "favicon.ico")
        filename = "{}_favicon.png".format(domain.replace(".", "_"))
        ok_icon = save_image_from_url(website, "favicon", icon_url, filename)
        if not ok_icon:
            website.favicon = None
        website.save()
    return website


def check_existing(url, artwork, model=None):
    u = base_url(url)
    return model.objects.filter(url=u, artwork=artwork).first() is not None


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument(
            '--delete',
            action='store_true',
            help='Delete existing query result',
        )
        parser.add_argument(
            '--only-images',
            action='store_true',
            default=False,
            help='Fetch only images',
        )

    @no_translations
    def handle(self, *args, **options):

        wikipedia.set_lang("it")

        if options.get("delete"):
            print("delete everything!")
            ArtworkQueryTextResult.objects.all().delete()
            ArtworkQueryImageResult.objects.all().delete()

        for artwork in Artwork.objects.all():
            print("- Processing artwork {}".format(artwork.title))
            if not options.get("only_images"):
                try:
                    page = wikipedia.page(artwork.title)
                    if not check_existing(page.url, artwork, ArtworkQueryTextResult):
                        website = create_website_for_url(page.url)
                        query_result = ArtworkQueryTextResult(
                            url=page.url,
                            body=page.summary,
                            title=page.title,
                            website=website,
                            artwork=artwork
                        )
                        query_result.save()
                        print("\t Wikipedia page saved correctly")
                    else:
                        print("\t Wikipedia page already in db")
                except wikipedia.exceptions.PageError:
                    print("no wikipedia pages found with the artwork title!")

                if ArtworkQueryTextResult.objects.filter(artwork=artwork).count() > 10:
                    continue

                for url in search(artwork.get_query(), stop=20, lang='it'):
                    if '.pdf' in url:
                        continue
                    try:
                        print("\t- url: {}".format(url))

                        if check_existing(url, artwork, ArtworkQueryTextResult):
                            print("\t\t skip! [already in db]")
                            continue

                        page = requests.get(url)
                        if page.status_code != 200:
                            print("\t\t skip! [status code {}]".format(page.status_code))
                            continue
                    except requests.exceptions.ContentDecodingError:
                        continue
                    except requests.exceptions.ConnectionError:
                        continue

                    website = create_website_for_url(url)

                    soup = BeautifulSoup(page.text, 'html.parser')
                    try:
                        title = soup.find("title").text
                        abstract = soup.find("title").text
                    except AttributeError:
                        continue

                    try:
                        abstract = soup.find("meta", {"name": "description"}).attrs['content']
                    except Exception:
                        pass
                    try:
                        abstract += sorted([p.text for p in soup.find_all("p")], key=lambda p: len(p), reverse=True)[0]
                    except IndexError:
                        continue

                    query_result = ArtworkQueryTextResult(
                        url=base_url(page.url),
                        body=abstract,
                        title=title,
                        website=website,
                        artwork=artwork
                    )
                    query_result.save()

            print("\n\t search for images")
            gis = GoogleImagesSearch(
                settings.GOOGLE_CUSTOMSEARCH_DEVELOPER_API_KEY,
                settings.GOOGLE_CUSTOMSEARCH_ENGINE_ID
            )
            search_params = {
                'q': artwork.get_query(),
                'num': 10,
                'safe': 'off',
                # 'imgSize': 'large'
            }
            gis.search(search_params=search_params)

            for google_image in gis.results():
                print("\t processing image {}".format(google_image.url))
                if google_image.url.split(".")[-1].lower() not in IMAGE_EXTENSIONS:
                    continue

                if check_existing(google_image.url, artwork, model=ArtworkQueryImageResult):
                    print("\t skip [already in db]")
                    continue

                website = create_website_for_url(google_image.url)
                query_image = ArtworkQueryImageResult(
                    url=base_url(google_image.url),
                    website=website,
                    artwork=artwork
                )
                extension = os.path.split(urlsplit(query_image.url).path)[-1].split(".")[-1]
                ok = save_image_from_url(query_image, "image", google_image.url, "{}.{}".format(uuid.uuid4(), extension))
                if ok:
                    query_image.save()
                    print("\t image saved")
                else:
                    print("\t skip [cannot save image]")
