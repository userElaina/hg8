#!/usr/bin/env python3

import os
from PIL import Image, ImageSequence

pth='flag.gif'
dirname=pth.split('.')[0]
os.makedirs(dirname,exist_ok=True)


im = Image.open(pth)

i = 0
for frame in ImageSequence.Iterator(im):
    frame.save(os.path.join(dirname,dirname+'_%d.png'%i))
    i+=1

