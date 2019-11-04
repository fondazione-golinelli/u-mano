import os

from umano.services.base import DataFetcher
from umano import settings


class IndianaJones(DataFetcher):

    def __init__(self, data_class="TestData", timeout=10) -> None:
        super().__init__(data_class, timeout)

    def process_data(self):
        super().process_data()