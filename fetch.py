import json
from apis.reddit import Reddit
from apis.coinpaprika import CoinPaprika
from variables import DATA_KEYS


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

        data_reddit = Reddit(obj['reddit']).reddit_data()
        data_coinpaprika = CoinPaprika().get_today_bitcoin()

        self.data[DATA_KEYS[0]] = data_reddit
        self.data[DATA_KEYS[1]] = data_coinpaprika

        return self.data
