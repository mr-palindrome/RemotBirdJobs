from flask import Flask, jsonify
from newscrap import scrape
import json

app = Flask(__name__)


# queries = {'1': 'remote developer hiring', '2': 'remote intern hiring'}


@app.route('/call/<string:query>')
def call(query):
    scrape(query)

    with open('tweets.json') as json_file:
        data = json.load(json_file)

    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
