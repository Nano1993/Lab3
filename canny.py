#! /usr/bin/env python


from SimpleCV import Camera, Display, Image
import time
import math
import matplotlib.pyplot as plt
import cv2.cv as cv2
import numpy as np

# Foto con fondo cuadrado
img= Image('/home/pi/Documents/Lab3/foto4.png')
(r,g,b)=img.splitChannels(False)

r.save('/home/pi/Documents/Lab3/red4.png')
g.save('/home/pi/Documents/Lab3/green4.png')
b.save('/home/pi/Documents/Lab3/blue4.png')


img=cv2.LoadImage('/home/pi/Documents/Lab3/foto4.png',cv2.CV_LOAD_IMAGE_GRAYSCALE)

pi=math.pi

dst = cv2.CreateImage(cv2.GetSize(img),8,1)
cv2.Canny(img,dst,100,200)
cv2.Threshold(dst,dst,100,255,cv2.CV_THRESH_BINARY)
color_dst_standard = cv2.CreateImage(cv2.GetSize(img),8,3)
cv2.CvtColor(img, color_dst_standard, cv2.CV_GRAY2BGR)
lines = cv2.HoughLines2(dst, cv2.CreateMemStorage(0), cv2.CV_HOUGH_STANDARD, 1, pi/180,100,0,0)
cv2.ShowImage('Image',img)
cv2.ShowImage("Cannied", dst)

cv2.WaitKey(0)





