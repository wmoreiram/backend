import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import base64
from io import BytesIO
import rasterio

dataset = rasterio.open('static/ndvi_4326.tif')
arr = dataset.read(1)
plt.hist(arr, bins='auto')  
plt.title("Histogram")
plt.show()

figfile = BytesIO()
plt.savefig(figfile, format='png')
img = base64.b64encode(figfile.read()).decode("UTF-8")
print(img)