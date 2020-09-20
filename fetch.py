import json
from apis.reddit import Reddit
from apis.coinpaprika import CoinPaprika
from apis.newsapi import NewsApi
from variables import DATA_KEYS, NEWSAPI_SOURCES_GENERAL, NEWSAPI_SOURCES_TECHNOLOGY


class Fetch():
    """Fetch data from all apis.
    """
    def __init__(self, path):
        self.filepath = path
        self.data = {}

    def fetch_all(self):
        """Fetch data from all data sources.
        """
        with open(self.filepath, 'r') as file:
            data = file.read()
        obj = json.loads(data)

        data_reddit = Reddit(obj['reddit']).get_data()
        data_newsapi_cz = NewsApi().get_data('top-headlines', 'country', 'cz')
        data_newsapi_general = NewsApi().get_data('top-headlines', 'sources', NEWSAPI_SOURCES_GENERAL)
        data_newsapi_technology = NewsApi().get_data('top-headlines', 'sources', NEWSAPI_SOURCES_TECHNOLOGY)
        data_coinpaprika = CoinPaprika().get_data()

        self.data[DATA_KEYS[0]] = data_reddit
        self.data[DATA_KEYS[1]] = data_newsapi_cz
        self.data[DATA_KEYS[2]] = data_newsapi_general
        self.data[DATA_KEYS[3]] = data_newsapi_technology
        self.data[DATA_KEYS[4]] = data_coinpaprika

        return self.data
