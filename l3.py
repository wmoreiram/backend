import geopyspark as gps
import matplotlib.pyplot as plt

from colortools import Color
from pyspark import SparkContext

conf = gps.geopyspark_conf(master="local[*]", appName="visualization")
pysc = SparkContext(conf=conf)

raster_layer = gps.geotiff.get(layer_type=gps.LayerType.SPATIAL, uri="true_color.tif")
tiled_layer = raster_layer.tile_to_layout(layout=gps.GlobalLayout(), target_crs=3857)

