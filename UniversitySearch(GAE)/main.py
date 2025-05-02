# main.py
from flask import Flask, request, jsonify, send_from_directory
import requests

app = Flask(__name__, static_folder='.', static_url_path='')

# Serve your static index.html and assets
@app.route('/', defaults={'path': 'index.html'})
@app.route('/<path:path>')
def static_proxy(path):
    return send_from_directory('.', path)

# Proxy endpoint
@app.route('/search')
def search_universities():
    q = request.args.get('name', '')
    # Server‐side HTTP fetch of the real API
    resp = requests.get(
        "http://universities.hipolabs.com/search",
        params={'name': q},
        timeout=10
    )
    return jsonify(resp.json())
