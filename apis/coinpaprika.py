import json
import requests


class CoinPaprika():
    """Get data from CoinPaprika api.
    """
    def __init__(self):
        self.api_url = 'https://api.coinpaprika.com/v1/'
        self.bitcoin_id = 'btc-bitcoin'

    async def get_data(self):
        """Get current price of btc.
        """
        url = f'{self.api_url}coins/btc-bitcoin/ohlcv/today'
        response = requests.get(url)
        return [
            {
                'coin': 'bitcoin',
                'price': json.loads(response.text)[0]['close']
            }
        ]
