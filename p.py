from flask import Flask, url_for
from flask_cors import CORS
import json
import rasterio

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/a")
def a():
    return "a"

@app.route("/inf")
def inf():
    meta = json.loads(open('static/meta.json').read())   
    dataset = rasterio.open('static/true_color_4326.tif')
    meta['bounds'] = dataset.bounds
    print(dataset.bounds)
    return json.dumps(meta), 200, {"Content-Type": "application/json"}

@app.route("/ndvi/<coord>")
def ndvi(coord):
    print(coord)
    return coord

app.run(debug=True, use_reloader=True)