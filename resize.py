from __future__ import division
from PIL import Image
from math import ceil
from sys import argv

fileName = argv[1]
maxwidth = int(argv[2])
maxheight = int(argv[3])

image = Image.open(fileName)
size = image.size

ratio = min(maxwidth/size[0], maxheight/size[1])

newsize = (int(ceil(ratio*size[0])), int(ceil(ratio*size[1])))

nearest = image.resize(newsize, Image.NEAREST)
bilinear = image.resize(newsize, Image.BILINEAR)
bicubic = image.resize(newsize, Image.BICUBIC)
antialias = image.resize(newsize, Image.ANTIALIAS)

nearest.save('nearest.jpg')
bilinear.save('bilinear.jpg')
bicubic.save('bicubic.jpg')
antialias.save('antialias.jpg')
