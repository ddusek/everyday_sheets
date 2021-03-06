import json
import asyncio
from data_apis.reddit import Reddit
from data_apis.coinpaprika import CoinPaprika
from data_apis.newsapi import NewsApi
from data_apis.newsapi_parameters import FIXED_PARAMS
from variables import DATA_KEYS, NEWSAPI_SOURCES_GENERAL, NEWSAPI_SOURCES_TECHNOLOGY, NEWSAPI_SOURCES_GAMING


class Fetch():
    """Fetch data from all apis.
    """
    def __init__(self, path=''):
        self.filepath = path
        self.data = {}

    def fetch_all(self):
        """Fetch data from all data sources.
        """
        with open(self.filepath, 'r') as file:
            data = file.read()
        reddit_input = json.loads(data)

        reddit = Reddit(reddit_input['reddit'])
        news_api = NewsApi()
        coin_paprika = CoinPaprika()

        data_reddit = asyncio.run(reddit.get_data())
        data_newsapi_cz = asyncio.run(news_api.get_data('top-headlines', 'country', 'cz'))
        data_newsapi_general = asyncio.run(news_api.get_data('top-headlines', 'sources', NEWSAPI_SOURCES_GENERAL))
        data_newsapi_technology = asyncio.run(news_api.get_data('top-headlines', 'sources', NEWSAPI_SOURCES_TECHNOLOGY))
        data_newsapi_science = asyncio.run(news_api.get_data('top-headlines', ['category', 'country'],
                                                                              ['science', 'us']))
        data_newsapi_gaming = asyncio.run(news_api.get_data('top-headlines', 'sources', NEWSAPI_SOURCES_GAMING))
        data_coinpaprika = asyncio.run(coin_paprika.get_data())

        self.data[DATA_KEYS[0]] = data_reddit
        self.data[DATA_KEYS[1]] = data_newsapi_cz
        self.data[DATA_KEYS[2]] = data_newsapi_general
        self.data[DATA_KEYS[3]] = data_newsapi_technology
        self.data[DATA_KEYS[4]] = data_newsapi_science
        self.data[DATA_KEYS[5]] = data_newsapi_gaming
        self.data[DATA_KEYS[6]] = data_coinpaprika

        return self.data

    def fetch_reddit(self):
        """Fetch reddit data.
        """
        with open(self.filepath, 'r') as file:
            data = file.read()
        reddit_input = json.loads(data)
        reddit = Reddit(reddit_input['reddit'])
        data = asyncio.run(reddit.get_data())
        return data

    def fetch_coinpaprika(self):
        """Fetch coinpaprika data.
        """
        coin_paprika = CoinPaprika()
        data = asyncio.run(coin_paprika.get_data())
        return data

    def fetch_newsapi(self, topic):
        """Fetch newsapi data according to topic in parameter.
        """
        newsapi = NewsApi()
        if topic not in FIXED_PARAMS:
            return {'error': f'topic {topic} not not'}
        data = asyncio.run(newsapi.get_data(*FIXED_PARAMS[topic]))
        return data
