from osgeo import gdal
dataset = gdal.Open('static/true_color_4326.tif',gdal.GA_ReadOnly)

print(dataset.GetMetadata())

print("Size is {} x {} x {}".format(dataset.RasterXSize,
                                    dataset.RasterYSize,
                                    dataset.RasterCount))
proj = dataset.GetProjection()

print("Projection is {}".format(dataset.GetProjection()))

srcband = dataset.GetRasterBand(1)

print("[ NO DATA VALUE ] = ", srcband.GetNoDataValue())
print("[ MIN ] = ", srcband.GetMinimum())
print("[ MAX ] = ", srcband.GetMaximum())
print("[ SCALE ] = ", srcband.GetScale())
print("[ UNIT TYPE ] = ", srcband.GetUnitType())
