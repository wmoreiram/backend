import rasterio
dataset = rasterio.open('lkklllltrue_color.tif')
print(dataset.name)
print(dataset.count)
print(dataset.bounds)
print(dataset.xy(dataset.width, dataset.height))
