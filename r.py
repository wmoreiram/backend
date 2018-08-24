import rasterio
dataset = rasterio.open('static/true_color_4326.tif')
print(dataset)
print(dataset.crs)
print(dataset.bounds)