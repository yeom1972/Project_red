import cv2
import numpy as np
from matplotlib import pyplot as plt
import ctypes

# Image Seclect
img_b = cv2.imread('C:\data\project\project1.jpg')
img_b2 = cv2.imread('C:\data\project\project1.jpg')
#img = cv2.imread('C:\data\project\project_small.jpg')
#img1 = cv2.imread('C:\data\project\project_small.jpg')
img = cv2.resize(img_b, dsize=(1280,960), fx=0.3, fy=0.7, interpolation=cv2.INTER_AREA)
img1 = cv2.resize(img_b2, dsize=(1280,960), fx=0.3, fy=0.7, interpolation=cv2.INTER_AREA)
h_base,w_base = img.shape[:2]

h = h_base//2
w = w_base//2

def BoundayXY(x,y,h_base,w_base): #x=0(left),1(right), y=0(down),1(up)
    moveH = 2*x - 1
    moveV = -2*y + 1
    f = open('C:\data\project\data.txt', 'w')
    HaccD = 0 #accumulated difference
    HmAccD = 0 #maximal of accumulated difference
    HcD = np.int32(0) #current difference
    HbCheck = 0 #boundary check
    Hmh = 0 #h with maximal
    Hmw = 0 #w with maximal
    h = h_base//2
    w = w_base//2
    for countH in range((h_base//2)-1):
        WaccD = 0 #accumulated difference
        WmAccD = 0 #maximal of accumulated difference
        WcD = np.int32(0) #current difference
        WbCheck = 0 #boundary check
        Wmh = 0 #h with maximal
        Wmw = 0 #w with maximal
        w = w_base//2
        HcP1 = np.int32((img[h,w])[2])
        #cv2.line(img1,(w,h),(w,h),(255,255,255))
        h = h + moveH
        HcD = HcP1 - np.int32((img[h,w])[2])
        #print(img[h,w][2])

        if HmAccD < HcD:
            HmAccD = HcD
            Hmh = h
            Hmw = w
        if HbCheck == 0 and HcD > 10:
            HbCheck = 1
        elif HbCheck == 1 and HcD < 7:
            cv2.line(img1,(Hmw,Hmh),(Hmw,Hmh),(255,255,255))
            #break;
        for countW in range((w_base//2)-1):
            WcP1 = np.int32((img[h,w])[2])
            #print(WcP1)
            #cv2.line(img1,(w,h),(w,h),(255,255,255))
            w = w + moveV
            WcD = WcP1 - np.int32((img[h,w])[2])
            #data_r = '{0}\n' .format(WcD)
            #f.write(data_r)
            #print(WcD)
            if WmAccD < WcD:
                WmAccD = WcD
                Wmh = h
                Wmw = w
            if WbCheck == 0 and WcD > 7:
                WbCheck = 1
                #print(WcD)
            elif WbCheck == 1 and WcD < 7:
                cv2.line(img1,(Wmw,Wmh),(Wmw,Wmh),(255,255,255))
                #break;

BoundayXY(0,0,h_base,w_base)
BoundayXY(1,0,h_base,w_base)
BoundayXY(0,1,h_base,w_base)
BoundayXY(1,1,h_base,w_base)

cv2.imshow('img1',img1)
cv2.imshow('img',img)
cv2.waitKey()
cv2.destroyAllWindows()
