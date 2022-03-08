from PIL import Image
from glob import glob
import os

for file in glob('ic_*'):
  #Open the image and convert in to RGB
  image = Image.open(file).convert('RGB')

  #Get the file name without the extension
  path, filename = os.path.split(file)
  filename = os.path.splitext(filename)[0]

  """
  Convert the image as requested:
  1. Rotate the image 90° clockwise
  2. Resize the image from 192x192 to 128x128
  3. Save the image to a new folder in .jpeg format
  """
  image.rotate(270).resize((128, 128)).save('/opt/icons/{}.jpeg'.format(filename))

print("Done  converting!")