from flask import Flask, request, url_for
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
    param = request.args.get("param")
    print(param)
    return param

@app.route("/inf")
def inf():
    meta = json.loads(open('static/meta.json').read())   
    dataset = rasterio.open('static/ndvi_4326.tif')
    meta['bounds'] = dataset.bounds
    print(dataset.bounds)
    return json.dumps(meta), 200, {"Content-Type": "application/json"}

@app.route("/ndvi")
def ndvi():
    param = request.args.get("param")
    dataset = rasterio.open('static/ndvi_4326.tif')
    band = dataset.read(1)
    width = dataset.width
    height = dataset.height
    coord = param.split(',')
    x = float(coord[0])
    y = float(coord[1])
    row, col = dataset.index(x,y)
    if (row > 0 and row <= height) and (col > 0 and col <= width) :
        ret = str(band[row, col])
    else :
        ret = ''
    print(ret)
    return ret

app.run(debug=True, use_reloader=True)