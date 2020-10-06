from flask import Flask, jsonify
from fetch import Fetch
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'hello world'


@app.route('/reddit')
def reddit():
    """Return reddit json data.
    """
    fetcher = Fetch('reddit_inputs.json')
    data = fetcher.fetch_reddit()
    return jsonify(data)


@app.route('/coinpaprika')
def coinpaprika():
    """Return coinpaprika json data.
    """
    fetcher = Fetch()
    data = fetcher.fetch_coinpaprika()
    return jsonify(data)


@app.route('/newsapi/<topic>')
def newsapi(topic):
    """Return newsapi json data according to topic.
    """
    fetcher = Fetch()
    data = fetcher.fetch_newsapi(topic)
    return jsonify(data)
