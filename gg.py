from osgeo import gdal
from numpy import *

g = gdal.Open('static/B03.TIF') # red band
band3 = g.ReadAsArray()
g = gdal.Open('static/B04.TIF') # near infrared band
band4 = g.ReadAsArray()

band4 = array(band4, dtype = float)  # change the array data type from integer to float to allow decimals
band3 = array(band3, dtype = float)
print(band4)
var1 = subtract(band4, band3) 
var2 = add(band4, band3)

ndvi = divide(var1,var2)
#print(ndvi)