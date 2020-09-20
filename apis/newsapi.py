import json
import requests
from variables import NEWSAPI_KEY, NEWSAPI_IGNORED_SOURCES


class NewsApi():
    """Get data from NewsApi.
    """
    def __init__(self):
        self.api_url = 'https://newsapi.org/v2/'

    def get_data(self, endpoint, parameter_key, parameter_value):
        """Get news according to parameters.

        :param endpoint: api endpoint for example: "top-headlines"
        :param parameter_key: parameter key for example: "sources"
        :param parameter_value: parameter value for example "abc-news,time"
        """
        url = f'{self.api_url}{endpoint}?apiKey={NEWSAPI_KEY}&{parameter_key}={parameter_value}'
        response = requests.get(url)
        results = []
        articles = json.loads(response.text)['articles']
        for article in articles:
            if parameter_key != 'sources' and article['source']['name'] in NEWSAPI_IGNORED_SOURCES:
                continue
            results.append({
                'title': article['title'],
                'url': article['url'],
                'time_published': article['publishedAt']
            })
        return results
