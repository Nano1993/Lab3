#! /usr/bin/env python

import time
from decimal import Decimal
import matplotlib.pyplot as plt
import cv2
import Image, numpy

epsilon = 0.6
Rho = numpy.array([0.29677419 ,0.25698324,0.19409283,0.36129032, 0.31284916, 0.23628692, 0.66451613, 0.57541899, 0.43459916])
img = cv2.imread('/home/pi/Documents/Lab3/Foto3.png',cv2.CV_LOAD_IMAGE_COLOR)
borde = 255*numpy.ones((480,640),float)
for i in range(1,479):
    for j in range(1,639):
        Xhr = float(img[i+1,j,0])
        Xhg = float(img[i+1,j,1])
        Xhb = float(img[i+1,j,2])
        Yhr = float(img[i-1,j,0])
        Yhg = float(img[i-1,j,1])
        Yhb = float(img[i-1,j,2])
        Xvr = float(img[i,j+1,0])
        Xvg = float(img[i,j+1,1])
        Xvb = float(img[i,j+1,2])
        Yvr = float(img[i,j-1,0])
        Yvg = float(img[i,j-1,1])
        Yvb = float(img[i,j-1,2])
        Xd1r = float(img[i+1,j+1,0])
        Xd1g = float(img[i+1,j+1,1])
        Xd1b = float(img[i+1,j+1,2])
        Yd1r = float(img[i-1,j-1,0])
        Yd1g = float(img[i-1,j-1,1])
        Yd1b = float(img[i-1,j-1,2])
        Xd2r = float(img[i-1,j+1,0])
        Xd2g = float(img[i-1,j+1,1])
        Xd2b = float(img[i-1,j+1,2])
        Yd2r = float(img[i+1,j-1,0])
        Yd2g = float(img[i+1,j-1,1])
        Yd2b = float(img[i+1,j-1,2])
        #if (Xhr==0 or Xhg==0 or Xhb==0 or Yhr==0 or Yhg==0 or Yhb==0 or Xvr==0 or Xvg==0 or Xvb==0 or Yvr==0 or Yvg==0 or Yvb==0 or Xd1r==0 or Xd1g==0 or Xd1b or Yd1r==0 or Yd1g==0 or Yd1b==0 or Xd2r==0 or Xd2g==0 or Xd2b==0 or Yd2r==0 or Yd2g==0 or Yd2b==0):
        #    continue
        rhoH1 = numpy.array([Xhr/Yhr,Xhr/Yhg,Xhr/Yhb,Xhg/Yhr,Xhg/Yhg,Xhg/Yhb,Xhb/Yhr,Xhb/Yhg,Xhb/Yhb])
        rhoH2 = numpy.array([Yhr/Xhr,Yhr/Xhg,Yhr/Xhb,Yhg/Xhr,Yhg/Xhg,Yhg/Xhb,Yhb/Xhr,Yhb/Xhg,Yhb/Xhb])
        rhoV1 = numpy.array([Xvr/Yvr,Xvr/Yvg,Xvr/Yvb,Xvg/Yvr,Xvg/Yvg,Xvg/Yvb,Xvb/Yvr,Xvb/Yvg,Xvb/Yvb])
        rhoV2 = numpy.array([Yvr/Xvr,Yvr/Xvg,Yvr/Xvb,Yvg/Xvr,Yvg/Xvg,Yvg/Xvb,Yvb/Xvr,Yvb/Xvg,Yvb/Xvb])
        rhoD11 = numpy.array([Xd1r/Yd1r,Xd1r/Yd1g,Xd1r/Yd1b,Xd1g/Yd1r,Xd1g/Yd1g,Xd1g/Yd1b,Xd1b/Yd1r,Xd1b/Yd1g,Xd1b/Yd1b])
        rhoD12 = numpy.array([Yd1r/Xd1r,Yd1r/Xd1g,Yd1r/Xd1b,Yd1g/Xd1r,Yd1g/Xd1g,Yd1g/Xd1b,Yd1b/Xd1r,Yd1b/Xd1g,Yd1b/Xd1b])
        rhoD21 = numpy.array([Xd2r/Yd2r,Xd2r/Yd2g,Xd2r/Yd2b,Xd2g/Yd2r,Xd2g/Yd2g,Xd2g/Yd2b,Xd2b/Yd2r,Xd2b/Yd2g,Xd2b/Yd2b])
        rhoD22 = numpy.array([Yd2r/Xd2r,Yd2r/Xd2g,Yd2r/Xd2b,Yd2g/Xd2r,Yd2g/Xd2g,Yd2g/Xd2b,Yd2b/Xd2r,Yd2b/Xd2g,Yd2b/Xd2b])

        if (max(abs(rhoH1-Rho))<epsilon):
            #print i
            #print j
            borde[i,j]=0
        if (max(abs(rhoH2-Rho))<epsilon):
            #print i
            #print j
            borde[i,j]=0
        if (max(abs(rhoV1-Rho))<epsilon):
            #print i
            #print j
            borde[i,j]=0
        if (max(abs(rhoV2-Rho))<epsilon):
            #print i
            #print j
            borde[i,j]=0
        if (max(abs(rhoD11-Rho))<epsilon):
            #print i
            #print j
            borde[i,j]=0
        if (max(abs(rhoD12-Rho))<epsilon):
            #print i
            #print j
            borde[i,j]=0
        if (max(abs(rhoD21-Rho))<epsilon):
            #print i
            #print j
            borde[i,j]=0
        if (max(abs(rhoD22-Rho))<epsilon):
            #print i
            #print j
            borde[i,j]=0
       
plt.imshow(borde,'gray')
plt.show()
cv2.waitKey(0)
