import json
import requests
from variables import NEWSAPI_KEY, NEWSAPI_IGNORED_SOURCES


class NewsApi():
    """Get data from NewsApi.
    """
    def __init__(self):
        self.api_url = 'https://newsapi.org/v2/'

    async def get_data(self, endpoint, parameter_key, parameter_value):
        """Get news according to parameters.

        :param endpoint: api endpoint for example: "top-headlines"
        :param parameter_key: parameter key for example: "sources". Can also be list of keys.
        :param parameter_value: parameter value for example "abc-news,time". Can also be list of values.
        """
        parameters = f'apiKey={NEWSAPI_KEY}'
        if isinstance(parameter_key, list) and isinstance(parameter_value, list):
            for key, value in zip(parameter_key, parameter_value):
                parameters += f'&{key}={value}'
        else:
            parameters += f'&{parameter_key}={parameter_value}'
        parameters += '&pageSize=10'

        url = f'{self.api_url}{endpoint}?{parameters}'
        response = requests.get(url)
        results = []
        articles = json.loads(response.text)['articles']
        for article in articles:
            if parameter_key != 'sources' and article['source']['name'] in NEWSAPI_IGNORED_SOURCES:
                continue
            results.append({
                'title': article['title'],
                'url': article['url'],
                'time_published': article['publishedAt'],
                'image': article['urlToImage']
            })
        return results
