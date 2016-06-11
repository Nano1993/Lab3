#! /usr/bin/env python

from SimpleCV import Camera, Display, Image
import time
import math
import matplotlib.pyplot as plt
import cv2.cv as cv
import numpy


#Tomar fotos
var = 'si'

while var == 'si' :
 print "Tomando fotografia..."
 c = Camera()
 time.sleep(2)
 img = c.getImage()
 img.show()
 var = raw_input("desea tomar la foto nuevamente: (si/no) ")

img.save('FotopruebaLab3.png')
(red,green,blue)=img.splitChannels(False)
red.save('red4.png')
green.save('green4.png')
blue.save('blue4.png')
imred=cv.LoadImage('/home/pi/Documents/Lab3/red4.png',cv.CV_LOAD_IMAGE_COLOR)
imgreen=cv.LoadImage('/home/pi/Documents/Lab3/green4.png',cv.CV_LOAD_IMAGE_COLOR)
imblue=cv.LoadImage('/home/pi/Documents/Lab3/blue4.png',cv.CV_LOAD_IMAGE_COLOR)

#carga de imagenes
orig = cv.LoadImage('FotopruebaLab3.png')
img=cv.LoadImage('FotopruebaLab3.png',cv.CV_LOAD_IMAGE_GRAYSCALE)
im=cv.LoadImage('/home/pi/Documents/Lab3/Foto4.png',cv.CV_LOAD_IMAGE_COLOR)

#division de imagenes
b = cv.CreateImage(cv.GetSize(orig), orig.depth, 1)
g = cv.CloneImage(b)
r = cv.CloneImage(b)
cv.Split(orig, b, g, r, None)

#combinar las 3 bandas 
merged = cv.CreateImage(cv.GetSize(orig), 8, 3)
cv.Merge(g, b, r, None, merged)

#despliege de imagenes
cv.ShowImage("Image", orig)
cv.ShowImage("Blue", b)
cv.ShowImage("Green", g)
cv.ShowImage("Red", r)
cv.ShowImage("Merged", merged)#merged=fucionado

cv.SaveImage("blue.png", b)
cv.SaveImage("verde.png", g)
cv.SaveImage("rojo.png", r)
cv.SaveImage("fucion.png",merged)#merged=fucionado
cv.WaitKey(0)
enter = raw_input("Mostrar Canny")
#canny
#imagen en gris
pi=math.pi
dst = cv.CreateImage(cv.GetSize(b),8,1)
cv.Canny(b,dst,100,200)
cv.Threshold(dst,dst,100,255,cv.CV_THRESH_BINARY)
color_dst_standard = cv.CreateImage(cv.GetSize(b),8,3)
cv.CvtColor(b, color_dst_standard, cv.CV_GRAY2BGR)
lines = cv.HoughLines2(dst, cv.CreateMemStorage(0), cv.CV_HOUGH_STANDARD, 1, pi/180,100,0,0)
cv.ShowImage("Greyscale edges canny", dst)
cv.SaveImage("Greyscale edges canny.png", dst)
cv.WaitKey(0)



#azul
pi=math.pi
dst = cv.CreateImage(cv.GetSize(b),8,1)
cv.Canny(b,dst,100,200)
cv.Threshold(dst,dst,100,255,cv.CV_THRESH_BINARY)
color_dst_standard = cv.CreateImage(cv.GetSize(b),8,3)
cv.CvtColor(b, color_dst_standard, cv.CV_GRAY2BGR)
lines = cv.HoughLines2(dst, cv.CreateMemStorage(0), cv.CV_HOUGH_STANDARD, 1, pi/180,100,0,0)
cv.ShowImage("blue edges canny", dst)
cv.SaveImage("blue edges canny.png", dst)
cv.WaitKey(0)

#verde
pi=math.pi
dst = cv.CreateImage(cv.GetSize(g),8,1)
cv.Canny(g,dst,100,200)
cv.Threshold(dst,dst,100,255,cv.CV_THRESH_BINARY)
color_dst_standard = cv.CreateImage(cv.GetSize(g),8,3)
cv.CvtColor(g, color_dst_standard, cv.CV_GRAY2BGR)
lines = cv.HoughLines2(dst, cv.CreateMemStorage(0), cv.CV_HOUGH_STANDARD, 1, pi/180,100,0,0)
cv.ShowImage("green edges canny", dst)
cv.SaveImage("green edges canny.png",dst)
cv.WaitKey(0)

#rojo
pi=math.pi
dst = cv.CreateImage(cv.GetSize(r),8,1)
cv.Canny(r,dst,100,200)
cv.Threshold(dst,dst,100,255,cv.CV_THRESH_BINARY)
color_dst_standard = cv.CreateImage(cv.GetSize(r),8,3)
cv.CvtColor(r, color_dst_standard, cv.CV_GRAY2BGR)
lines = cv.HoughLines2(dst, cv.CreateMemStorage(0), cv.CV_HOUGH_STANDARD, 1, pi/180,100,0,0)
cv.ShowImage("red edges canny", dst)
cv.SaveImage("red edges canny.png",dst)
cv.WaitKey(0)

enter = raw_input("Mostrar Sobel")
# sobel
#imagen en gris
sobx = cv.CreateImage(cv.GetSize(img), cv.IPL_DEPTH_16S, 1)
cv.Sobel(img, sobx, 1, 0, 3) #Sobel with x-order=1

soby = cv.CreateImage(cv.GetSize(img), cv.IPL_DEPTH_16S, 1)
cv.Sobel(img, soby, 0, 1, 3) #Sobel withy-oder=1

cv.Abs(sobx, sobx)
cv.Abs(soby, soby)

result = cv.CloneImage(img)
cv.Add(sobx, soby, result) #Add the two results together.

cv.Threshold(result, result, 100, 255, cv.CV_THRESH_BINARY_INV)
cv.ShowImage('Grayscale edge Sobel', result)
cv.SaveImage("Grayscale edge Sobel.png",dst)
cv.WaitKey(0)
#azul
sobx = cv.CreateImage(cv.GetSize(b), cv.IPL_DEPTH_16S, 1)
cv.Sobel(b, sobx, 1, 0, 3) #Sobel with x-order=1

soby = cv.CreateImage(cv.GetSize(b), cv.IPL_DEPTH_16S, 1)
cv.Sobel(b, soby, 0, 1, 3) #Sobel withy-oder=1

cv.Abs(sobx, sobx)
cv.Abs(soby, soby)

result = cv.CloneImage(b)
cv.Add(sobx, soby, result) #Add the two results together.

cv.Threshold(result, result, 100, 255, cv.CV_THRESH_BINARY_INV)
cv.ShowImage('blue edge Sobel', result)
cv.SaveImage("blue edge Sobel.png",dst)
cv.WaitKey(0)
#rojo
sobx = cv.CreateImage(cv.GetSize(r), cv.IPL_DEPTH_16S, 1)
cv.Sobel(r, sobx, 1, 0, 3) #Sobel with x-order=1

soby = cv.CreateImage(cv.GetSize(r), cv.IPL_DEPTH_16S, 1)
cv.Sobel(r, soby, 0, 1, 3) #Sobel withy-oder=1

cv.Abs(sobx, sobx)
cv.Abs(soby, soby)

result = cv.CloneImage(r)
cv.Add(sobx, soby, result) #Add the two results together.

cv.Threshold(result, result, 100, 255, cv.CV_THRESH_BINARY_INV)
cv.ShowImage('red edge Sobel', result)
cv.SaveImage("red edge Sobel.png",dst)
cv.WaitKey(0)
#green
sobx = cv.CreateImage(cv.GetSize(g), cv.IPL_DEPTH_16S, 1)
cv.Sobel(g, sobx, 1, 0, 3) #Sobel with x-order=1

soby = cv.CreateImage(cv.GetSize(g), cv.IPL_DEPTH_16S, 1)
cv.Sobel(g, soby, 0, 1, 3) #Sobel withy-oder=1

cv.Abs(sobx, sobx)
cv.Abs(soby, soby)

result = cv.CloneImage(g)
cv.Add(sobx, soby, result) #Add the two results together.

cv.Threshold(result, result, 100, 255, cv.CV_THRESH_BINARY_INV)
cv.ShowImage('green edge Sobel', result)
cv.SaveImage("green edge Sobel.png",dst)
cv.WaitKey(0)
enter = raw_input("Mostrar Morphed")
#morphel
#imagen en gris
morphed = cv.CloneImage(img)
cv.MorphologyEx(img, morphed, None, None, cv.CV_MOP_GRADIENT) # Apply a dilate - Erode

cv.Threshold(morphed, morphed, 30, 255, cv.CV_THRESH_BINARY_INV)
cv.ShowImage("Morphed Grayscale edge", morphed)
cv.SaveImage("Grayscale edge Morphed.png",dst)
cv.WaitKey(0)

#blue
morphed = cv.CloneImage(b)
cv.MorphologyEx(b, morphed, None, None, cv.CV_MOP_GRADIENT) # Apply a dilate - Erode

cv.Threshold(morphed, morphed, 30, 255, cv.CV_THRESH_BINARY_INV)
cv.ShowImage("Morphed blue edge", morphed)
cv.SaveImage("blue edge Morphed.png",dst)
cv.WaitKey(0)

#red
morphed = cv.CloneImage(r)
cv.MorphologyEx(r, morphed, None, None, cv.CV_MOP_GRADIENT) # Apply a dilate - Erode

cv.Threshold(morphed, morphed, 30, 255, cv.CV_THRESH_BINARY_INV)
cv.ShowImage("Morphed red edge", morphed)
cv.SaveImage("red edge Morphed.png",dst)
cv.WaitKey(0)

#green
morphed = cv.CloneImage(g)
cv.MorphologyEx(g, morphed, None, None, cv.CV_MOP_GRADIENT) # Apply a dilate - Erode

cv.Threshold(morphed, morphed, 30, 255, cv.CV_THRESH_BINARY_INV)
cv.ShowImage("Morphed green edge", morphed)
cv.SaveImage("green edge Morphed.png",dst)
cv.WaitKey(0)

enter = raw_input("Mostrar Laplace")

#laplace
#imagen en gris
gray=cv.CreateImage(cv.GetSize(im),8,1)
cv.CvtColor(im,gray,cv.CV_BGR2GRAY)
aperture=3 #cambiar el aperture
dst=cv.CreateImage(cv.GetSize(gray),cv.IPL_DEPTH_32F,1)
cv.Laplace(gray,dst,aperture)
cv.Convert(dst,gray)
thresholded=cv.CloneImage(im)
cv.Threshold(orig,thresholded,100,255,cv.CV_THRESH_BINARY_INV)

cv.ShowImage('Grayscale edge Laplace',gray)
cv.SaveImage("Grayscale edge Laplace.png",dst)
cv.WaitKey(0)
#azul
blue=cv.CreateImage(cv.GetSize(imblue),8,1)
cv.CvtColor(im,blue,cv.CV_BGR2GRAY)
aperture=3 #cambiar el aperture
dst=cv.CreateImage(cv.GetSize(blue),cv.IPL_DEPTH_32F,1)
cv.Laplace(blue,dst,aperture)
cv.Convert(dst,blue)
thresholded=cv.CloneImage(im)
cv.Threshold(orig,thresholded,100,255,cv.CV_THRESH_BINARY_INV)

cv.ShowImage('blue edge Laplace',blue)
cv.SaveImage("blue edge Laplace.png",dst)
cv.WaitKey(0)
#rojo
red=cv.CreateImage(cv.GetSize(imred),8,1)
cv.CvtColor(im,red,cv.CV_BGR2GRAY)
aperture=3 #cambiar el aperture
dst=cv.CreateImage(cv.GetSize(red),cv.IPL_DEPTH_32F,1)
cv.Laplace(red,dst,aperture)
cv.Convert(dst,red)
thresholded=cv.CloneImage(im)
cv.Threshold(orig,thresholded,100,255,cv.CV_THRESH_BINARY_INV)

cv.ShowImage('red edge Laplace',red)
cv.SaveImage("red edge Laplace.png",dst)
cv.WaitKey(0)
#green
green=cv.CreateImage(cv.GetSize(imgreen),8,1)
cv.CvtColor(im,green,cv.CV_BGR2GRAY)
aperture=3 #cambiar el aperture
dst=cv.CreateImage(cv.GetSize(green),cv.IPL_DEPTH_32F,1)
cv.Laplace(green,dst,aperture)
cv.Convert(dst,green)
thresholded=cv.CloneImage(im)
cv.Threshold(orig,thresholded,100,255,cv.CV_THRESH_BINARY_INV)

cv.ShowImage('grenn edge Laplace',green)
cv.SaveImage("green edge Laplace.png",dst)
cv.WaitKey(0)

enter = raw_input("Mostrar Harrys")

#harrys
dst_32f = cv.CreateImage(cv.GetSize(img), cv.IPL_DEPTH_32F, 1)

neighbourhood = 3
aperture = 3
k = 0.01
maxStrength = 0.0
threshold = 0.01
nonMaxSize = 3

cv.CornerHarris(img, dst_32f, neighbourhood, aperture, k)

minv, maxv, minl, maxl = cv.MinMaxLoc(dst_32f)

dilated = cv.CloneImage(dst_32f)
cv.Dilate(dst_32f, dilated)#nos aseguramos que el pixel local su maximo valor no cambia y todos los otros pixeles si 

localMax = cv.CreateMat(dst_32f.height, dst_32f.width, cv.CV_8U)
cv.Cmp(dst_32f, dilated, localMax, cv.CV_CMP_EQ)#comparamos y guardamos solo los pixeles modificados los que son los maximos valores locales que son esquinas 

threshold = 0.01 * maxv
cv.Threshold(dst_32f, dst_32f, threshold, 255, cv.CV_THRESH_BINARY)

cornerMap = cv.CreateMat(dst_32f.height, dst_32f.width, cv.CV_8U)
cv.Convert(dst_32f, cornerMap) #convertir y utilizar la operacion logica AND
cv.And(cornerMap, localMax, cornerMap) #Borrar todos los pixeles modificados

radius = 3
thickness = 2

l = []
for x in range(cornerMap.height):# crea la lista de todos los pixeles que no son 0 (no negro)
    
    for y in range(cornerMap.width):
        if cornerMap[x,y]:
            l.append((y,x))

for center in l:
    cv.Circle(img, center, radius, (255,255,255), thickness)


cv.ShowImage("Grayscale CornerHarris Result", dst_32f)
cv.ShowImage("Unique Points after Dilatation/CMP/And", cornerMap)
cv.SaveImage("Grayscale corner Harris.png",dst_32f)
cv.SaveImage("Unique Points after Dilatation/CMP/And.png",cornerMap)
cv.WaitKey(0)

#azul
dst_32f = cv.CreateImage(cv.GetSize(b), cv.IPL_DEPTH_32F, 1)

neighbourhood = 3
aperture = 3
k = 0.01
maxStrength = 0.0
threshold = 0.01
nonMaxSize = 3

cv.CornerHarris(b, dst_32f, neighbourhood, aperture, k)

minv, maxv, minl, maxl = cv.MinMaxLoc(dst_32f)

dilated = cv.CloneImage(dst_32f)
cv.Dilate(dst_32f, dilated) 

localMax = cv.CreateMat(dst_32f.height, dst_32f.width, cv.CV_8U)
cv.Cmp(dst_32f, dilated, localMax, cv.CV_CMP_EQ) 

threshold = 0.01 * maxv
cv.Threshold(dst_32f, dst_32f, threshold, 255, cv.CV_THRESH_BINARY)

cornerMap = cv.CreateMat(dst_32f.height, dst_32f.width, cv.CV_8U)
cv.Convert(dst_32f, cornerMap) 
cv.And(cornerMap, localMax, cornerMap) 

radius = 3
thickness = 2

l = []
for x in range(cornerMap.height): 
    for y in range(cornerMap.width):
        if cornerMap[x,y]:
            l.append((y,x))

for center in l:
    cv.Circle(b, center, radius, (255,255,255), thickness)


cv.ShowImage("Blue CornerHarris Result", dst_32f)
cv.ShowImage("Unique Points after Dilatation/CMP/And", cornerMap)
cv.SaveImage("Blue corner Harris.png", dst_32f)
cv.SaveImage("Unique Points after Dilatation/CMP/And.png",cornerMap)
cv.WaitKey(0)

#red
dst_32f = cv.CreateImage(cv.GetSize(r), cv.IPL_DEPTH_32F, 1)

neighbourhood = 3
aperture = 3
k = 0.01
maxStrength = 0.0
threshold = 0.01
nonMaxSize = 3

cv.CornerHarris(r, dst_32f, neighbourhood, aperture, k)

minv, maxv, minl, maxl = cv.MinMaxLoc(dst_32f)

dilated = cv.CloneImage(dst_32f)
cv.Dilate(dst_32f, dilated) 

localMax = cv.CreateMat(dst_32f.height, dst_32f.width, cv.CV_8U)
cv.Cmp(dst_32f, dilated, localMax, cv.CV_CMP_EQ) 

threshold = 0.01 * maxv
cv.Threshold(dst_32f, dst_32f, threshold, 255, cv.CV_THRESH_BINARY)

cornerMap = cv.CreateMat(dst_32f.height, dst_32f.width, cv.CV_8U)
cv.Convert(dst_32f, cornerMap) 
cv.And(cornerMap, localMax, cornerMap) 

radius = 3
thickness = 2

l = []
for x in range(cornerMap.height): 
    for y in range(cornerMap.width):
        if cornerMap[x,y]:
            l.append((y,x))

for center in l:
    cv.Circle(r, center, radius, (255,255,255), thickness)


cv.ShowImage("Red CornerHarris Result", dst_32f)
cv.ShowImage("Unique Points after Dilatation/CMP/And", cornerMap)
cv.SaveImage("Red corner Harris.png", dst_32f)
cv.SaveImage("Unique Points after Dilatation/CMP/And.png",cornerMap)
cv.WaitKey(0)
#green

dst_32f = cv.CreateImage(cv.GetSize(g), cv.IPL_DEPTH_32F, 1)

neighbourhood = 3
aperture = 3
k = 0.01
maxStrength = 0.0
threshold = 0.01
nonMaxSize = 3

cv.CornerHarris(g, dst_32f, neighbourhood, aperture, k)

minv, maxv, minl, maxl = cv.MinMaxLoc(dst_32f)

dilated = cv.CloneImage(dst_32f)
cv.Dilate(dst_32f, dilated) 

localMax = cv.CreateMat(dst_32f.height, dst_32f.width, cv.CV_8U)
cv.Cmp(dst_32f, dilated, localMax, cv.CV_CMP_EQ) 

threshold = 0.01 * maxv
cv.Threshold(dst_32f, dst_32f, threshold, 255, cv.CV_THRESH_BINARY)

cornerMap = cv.CreateMat(dst_32f.height, dst_32f.width, cv.CV_8U)
cv.Convert(dst_32f, cornerMap) 
cv.And(cornerMap, localMax, cornerMap) 

radius = 3
thickness = 2

l = []
for x in range(cornerMap.height): 
    for y in range(cornerMap.width):
        if cornerMap[x,y]:
            l.append((y,x))

for center in l:
    cv.Circle(g, center, radius, (255,255,255), thickness)


cv.ShowImage("Green CornerHarris Result", dst_32f)
cv.ShowImage("Unique Points after Dilatation/CMP/And", cornerMap)
cv.SaveImage("Green corner Harris.png", dst_32f)
cv.SaveImage("Unique Points after Dilatation/CMP/And.png",cornerMap)
cv.WaitKey(0)


enter = raw_input("Mostrar Borde alternativo")

#detector de borde alternativo 
im2 = cv.CreateImage(cv.GetSize(orig), 8, 1)
cv.CvtColor(orig, im2, cv.CV_BGR2GRAY)
#mantiene el color original y dibuja el conrto al final 

cv.Threshold(im2, im2, 128, 255, cv.CV_THRESH_BINARY)
cv.ShowImage("Threshold 1", im2)

element = cv.CreateStructuringElementEx(5*2+1, 5*2+1, 5, 5, cv.CV_SHAPE_RECT)

cv.MorphologyEx(im2, im2, None, element, cv.CV_MOP_OPEN)#habre y cierra para que aparesca el contorno
cv.MorphologyEx(im2, im2, None, element, cv.CV_MOP_CLOSE)
cv.Threshold(im2, im2, 128, 255, cv.CV_THRESH_BINARY_INV)
cv.ShowImage("After MorphologyEx", im2)
# --------------------------------

vals = cv.CloneImage(im2)#crea y clona para encontrar los contrnos de la imagen modificada
contours=cv.FindContours(vals, cv.CreateMemStorage(0), cv.CV_RETR_LIST, cv.CV_CHAIN_APPROX_SIMPLE, (0,0))

_red = (0, 0, 255); #contorno rojo
_green = (0, 255, 0);#contorno verde
levels=2 #1 dibuja un contorno o mas en este caso es 2
cv.DrawContours (orig, contours, _red, _green, levels, 2, cv.CV_FILLED)#dibujar los contornos de color de imagenes

cv.ShowImage("Image", orig)
cv.SaveImage("Bordes imagen.png",orig)
cv.WaitKey(0)
enter = raw_input("Mostrar Borde implementado por el profesor")

epsilon = 0.5
Rho = numpy.array([0.29677419 ,0.25698324,0.19409283,0.36129032, 0.31284916, 0.23628692, 0.66451613, 0.57541899, 0.43459916])
img = cv2.imread('FotopruebaLab3.png',cv2.CV_LOAD_IMAGE_COLOR)
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
