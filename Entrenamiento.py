#! /usr/bin/env python

from SimpleCV import Camera, Display, Image
import time
import math
import matplotlib.pyplot as plt
import cv2
import numpy


contL =  numpy.array([0,0,0])
contP =  numpy.array([0,0,0])
a = numpy.array([0,0,0])
b = numpy.array([0,0,0])
for s in range(1,2):
    if (s==1):
        img = cv2.imread('/home/pi/Documents/Lab3/Foto1.png',cv2.CV_LOAD_IMAGE_COLOR)
        ret3,th3 = cv2.threshold(img,130,255,cv2.THRESH_BINARY)
    if (s==2):
        img = cv2.imread('/home/pi/Documents/Lab3/Foto2.png',cv2.CV_LOAD_IMAGE_COLOR)
        ret3,th3 = cv2.threshold(img,100,255,cv2.THRESH_BINARY)
    if (s==3):
        img = cv2.imread('/home/pi/Documents/Lab3/Foto3.png',cv2.CV_LOAD_IMAGE_COLOR)
        ret3,th3 = cv2.threshold(img,120,255,cv2.THRESH_BINARY)
    if (s==4):
        img = cv2.imread('/home/pi/Documents/Lab3/Foto4.png',cv2.CV_LOAD_IMAGE_COLOR)
        ret3,th3 = cv2.threshold(img,80,255,cv2.THRESH_BINARY)
    if (s==5):
        img = cv2.imread('/home/pi/Documents/Lab3/Foto5.png',cv2.CV_LOAD_IMAGE_COLOR)
        ret3,th3 = cv2.threshold(img,100,255,cv2.THRESH_BINARY)
    if (s==6):
        img = cv2.imread('/home/pi/Documents/Lab3/Foto6.png',cv2.CV_LOAD_IMAGE_COLOR)
        ret3,th3 = cv2.threshold(img,110,255,cv2.THRESH_BINARY)
    if (s==7):
        img = cv2.imread('/home/pi/Documents/Lab3/Foto7.png',cv2.CV_LOAD_IMAGE_COLOR)
        ret3,th3 = cv2.threshold(img,100,255,cv2.THRESH_BINARY)
   


    for k in range(0,3):
        for i in range(0,480):
            for j in range(0,640):
                c = th3[i,j]
                if (not(any(c))):
                    a[k]=a[k]+img[i,j,k]
                    contL[k]=contL[k]+1
                else:
                    b[k]=b[k]+img[i,j,k]
                    contP[k]=contP[k]+1
Ar = float(a[0]/contL[0])
Ag = float(a[1]/contL[1])
Ab = float(a[2]/contL[2])
Br = float(b[0]/contP[0])
Bg = float(b[1]/contP[1])
Bb = float(b[2]/contP[2])   

Rho = numpy.array([Ar/Br,Ar/Bg,Ar/Bb,Ag/Br,Ag/Bg,Ag/Bb,Ab/Br,Ab/Bg,Ab/Bb])
print(Rho)

 

