from pyspark import SparkContext

import geopyspark as gps

conf = gps.geopyspark_conf(master="local[*]", appName="ingest-example")
pysc = SparkContext(conf=conf)

raster_layer = gps.geotiff.get(layer_type=gps.LayerType.SPATIAL, uri="file://true_color.tif")

tiled_raster_layer = raster_layer.tile_to_layout(gps.GlobalLayout(), target_crs=3857)

pyramided_layer = tiled_raster_layer.pyramid()

for tiled_layer in pyramided_layer.levels.values():
    gps.write(uri="file://ingested-image", layer_name="true-color", tiled_raster_layer=tiled_layer)