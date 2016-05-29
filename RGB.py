#! /usr/bin/env python
from SimpleCV import Camera, Display, Image
import time
import matplotlib.pyplot as plt
import cv2
import numpy as np


img= Image('/home/pi/Documents/Lab3/foto4.png')
(r,g,b)=img.splitChannels(False)

r.save('/home/pi/Documents/Lab3/red4.png')
g.save('/home/pi/Documents/Lab3/green4.png')
b.save('/home/pi/Documents/Lab3/blue4.png')


#b,g,r=cv2.split(img)
#img=cv2.merge((b,g,r))
