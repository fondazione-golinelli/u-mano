import random
import json
import os
import shutil
import time
from optparse import make_option

import requests

from googlesearch import search
from google_images_download import google_images_download
from bs4 import BeautifulSoup

from hal.data import store, find
from hal.models import QueryImageResult, QueryWebResult
from umano.services.base import UmanoService

from umano import settings


class GoogleQuery(UmanoService):
    option_list = UmanoService.option_list + [
        make_option(
            '--query',
            dest='QUERY',
            type=str,
            default="battaglia di anghiari leonardo",
            help='query to look from on the web'
        )
    ]

    def __init__(self) -> None:
        super().__init__()
        self.name = "Google query text service"
        self.description = "Make text queries and store result in db"
        self.pause = 5
        self.start = 0
        self.query = ""
        self.num = 10
        self.max_text = 256
        self.output_directory = settings.QUERY_SHARE_FOLDER
        self.timeout = 10
        self.image_downloader = google_images_download.googleimagesdownload()
        self.limit = 100

    def process_args_and_options(self, args, options):
        super().process_args_and_options(args, options)
        self.query = options.QUERY

    def get_suggested_queries(self, query):
        URL = "http://suggestqueries.google.com/complete/search?client=firefox&q={}".format(query)
        headers = {'User-agent': 'Mozilla/5.0'}
        response = requests.get(URL, headers=headers)
        result = json.loads(response.content.decode('utf-8'))
        return result

    def execute(self, args, options):
        while True:
            query = self.query
            if len(find(QueryWebResult, query={"query": self.query})) > self.limit:
                suggested_queries = self.get_suggested_queries(query)
                query = suggested_queries[1][random.randint(1, len(suggested_queries[1])-1)]
                self.log(msg="changing query from {} to {}".format(self.query, query))
            start = len(find(QueryWebResult, query={"query": query}))
            for url in search(query, lang="it", safe="on", num=self.num, start=start, stop=self.num,
                              pause=self.pause, only_standard=True):
                if '.pdf' in url:
                    continue
                try:
                    self.log(msg="\t- processing web url: {}".format(url))

                    if len(find(QueryWebResult, query={"url": url}, limit=1)) > 0:
                        self.log("already in db, skip")
                        continue

                    page = requests.get(url)
                    if page.status_code != 200:
                        continue

                except requests.exceptions.ContentDecodingError:
                    continue
                except requests.exceptions.ConnectionError:
                    continue

                html = BeautifulSoup(page.text, 'html.parser')
                lines = []
                try:
                    lines.append(html.find("title").text)
                except AttributeError:
                    continue

                try:
                    lines.append(html.find("meta", {"name": "description"}).attrs['content'])
                except Exception:
                    pass

                ps = sorted([p.text for p in html.find_all("p")], key=lambda p: len(p), reverse=True)
                for p in ps:
                    lines.append(p)
                text = "\n".join(lines)[:4096]

                store(
                    data_class=QueryWebResult,
                    data=dict(
                        query=self.query,
                        url=url,
                        text=text
                    ),
                    publish_after=True
                )
                self.log(msg="saved query text from url {}".format(url))

            start = len(find(QueryImageResult, query={"query": query}))
            image_paths = self.image_downloader.download(
                dict(keywords=query, limit=start+self.num, offset=start, save_source="output", chromedriver="C:\\Users\\u-man\\Desktop\\chromedriver.exe"))

            output_file = os.path.join(os.getcwd(), "downloads", "output.txt")

            with open(output_file, "r") as f:
                for line in f.read().split("\n"):
                    if "\t" not in line:
                        continue
                    path, url = line.split("\t")
                    if len(find(QueryImageResult, query={"url": url}, limit=1)) > 0:
                        self.log("already in db, skip")
                        continue
                    extension = path.split(".")[-1]
                    query_image = store(
                        data_class=QueryImageResult,
                        data=dict(
                            query=self.query,
                            url=url,
                            src=""
                        ),
                        publish_after=False
                    )
                    output_path = os.path.normpath(os.path.join(self.output_directory, "{}.{}".format(query_image.pk, extension)))
                    shutil.move(os.path.join(os.getcwd(), path), output_path)
                    query_image.src = output_path
                    query_image.save()

            with open(output_file, "w") as f:
                f.close()

            self.start += self.num
            time.sleep(self.timeout)


if __name__ == "__main__":
    service = GoogleQuery()
    service.run()
