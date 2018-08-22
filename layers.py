import geopyspark as gps

from pyspark import SparkContext
from shapely.geometry import box

conf = gps.geopyspark_conf(appName="layers", master="local[*]")
sc = SparkContext(conf=conf)

raster_layer = gps.geotiff.get(layer_type=gps.LayerType.SPATIAL,
                               uri='true_color.tif',
                               num_partitions=100)

tiled_layer = raster_layer.tile_to_layout(layout=gps.GlobalLayout(), target_crs=4326)

area_of_interest = box(-45.813981, -10.575509, -45.762979, -10.575636)

masked = tiled_layer.mask(geometries=area_of_interest)

pyramided_mask = masked.pyramid()

for pyramid in pyramided_mask.levels.values():
    gps.write(uri='file://pa-nlcd-2011',
              layer_name='true-color',
              tiled_raster_layer=pyramid)