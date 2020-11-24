#!flask/bin/python
from flask import Flask, jsonify
from flask import request
from flask import make_response
from flask import abort

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

import os

app = Flask(__name__)

@app.route('/yamap/api/v1.0/fromGlobalPixels', methods=['POST'])
def create_task():
    if not request.json or not 'x' in request.json or not 'y' in request.json or not 'zoom' in request.json:
        abort(400)
    x = request.json['x'];
    y = request.json['y'];
    zoom = request.json['zoom'];

    return jsonify({'coordinates': [x, y, zoom]}), 200

if __name__ == '__main__':
    opts = Options()
    opts.set_headless()
    assert opts.headless  # без графического интерфейса.

    browser = Firefox(options=opts)
    browser.get('index.html')

    app.run(debug=True)
