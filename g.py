from osgeo import gdal
import numpy as np

dataset = gdal.Open('static/ndvi_4326.tif',gdal.GA_ReadOnly)
band = dataset.GetRasterBand(1)
ds = band.GetDataset()
f = ds.GetNextFeature()
scanline = band.ReadRaster(xoff=0, yoff=0,
                           xsize=band.XSize, ysize=1,
                           buf_xsize=band.XSize, buf_ysize=1,
                           buf_type=gdal.GDT_Float32)
print(scanline)