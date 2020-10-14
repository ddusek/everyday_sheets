from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from fetch import Fetch
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
@cross_origin()
def hello_world():
    """Just for test functionality.
    """
    return 'hello world'


@app.route('/reddit')
@cross_origin()
def reddit():
    """Return reddit json data.
    """
    fetcher = Fetch('reddit_inputs.json')
    data = fetcher.fetch_reddit()
    return jsonify(data)


@app.route('/coinpaprika')
@cross_origin()
def coinpaprika():
    """Return coinpaprika json data.
    """
    fetcher = Fetch()
    data = fetcher.fetch_coinpaprika()
    return jsonify(data)


@app.route('/newsapi/<topic>')
@cross_origin()
def newsapi(topic):
    """Return newsapi json data according to topic.
    """
    fetcher = Fetch()
    data = fetcher.fetch_newsapi(topic)
    return jsonify(data)
