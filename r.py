import rasterio
import numpy
import rasterio.features
import rasterio.warp
from osgeo import ogr

dataset = rasterio.open('static/ndvi_4326.tif')
band = dataset.read(1)
width = dataset.width
height = dataset.height
param = '-45.785919117040606,-10.62006139237969'
#param = '-47.785919117040606,-9.62006139237969'
coord = param.split(',')
x = float(coord[0])
y = float(coord[1])
row, col = dataset.index(x,y)
#row, col = dataset.index(-46.6666,-9.62006)
if (row > 0 and row <= height) and (col > 0 and col <= width) :
  val = str(band[row, col])
else :
  val = 'vazio'
print(val)

#with rasterio.open('static/true_color_4326.tif') as dataset:

    # Read the dataset's valid data mask as a ndarray.
    #mask = dataset.dataset_mask()

    # Extract feature shapes and values from the array.

    #feature = rasterio.features.shapes(mask, transform=dataset.transform)

    #for geom, val in rasterio.features.shapes(
     #       mask, transform=dataset.transform):
      #  print(geom)
        #point = ogr.CreateGeometryFromJson(geom)
