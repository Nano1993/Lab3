#! /usr/bin/env python
from SimpleCV import Camera, Display, Image
import time
import matplotlib.pyplot as plt
import cv2
import numpy as np

import cv2.cv as cv

img= Image('/home/pi/Documents/Lab3/foto4.png')
(r,g,b)=img.splitChannels(False)

r.save('/home/pi/Documents/Lab3/red4.png')
g.save('/home/pi/Documents/Lab3/green4.png')
b.save('/home/pi/Documents/Lab3/blue4.png')

im=cv.LoadImage('/home/pi/Documents/Lab3/green4.png',cv.CV_LOAD_IMAGE_COLOR)

gray=cv.CreateImage(cv.GetSize(im),8,1)
cv.CvtColor(im,gray,cv.CV_BGR2GRAY)

aperture=3

dst=cv.CreateImage(cv.GetSize(gray),cv.IPL_DEPTH_32F,1)
cv.Laplace(gray,dst,aperture)

cv.Convert(dst,gray)

thresholded=cv.CloneImage(im)
cv.Threshold(im,thresholded,100,255,cv.CV_THRESH_BINARY_INV)

cv.ShowImage('Laplaced grayscale',gray)
cv.WaitKey(0)

