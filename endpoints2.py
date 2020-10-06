from flask import Flask
from fetch import Fetch
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'hello world'


@app.route('/reddit')
def reddit():
    fetcher = Fetch('../reddit_inputs.json')
    data = fetcher.fetch_reddit()
    return data
