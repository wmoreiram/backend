import rasterio
from matplotlib import pyplot
dataset = rasterio.open('true_color.tif')
print(dataset.name)
print(dataset.bounds)
array = dataset.read(1)
pyplot.imshow(array, cmap='pink')
pyplot.show()  
dataset.closed
