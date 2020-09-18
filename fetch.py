import json
from apis.reddit import Reddit


class Fetch():
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

        self.data['reddit'] = data_reddit

        return data
