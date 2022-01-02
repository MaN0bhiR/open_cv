import cv2
import numpy as np
width = 640
height = 360
my_cam = cv2.VideoCapture(0)

my_cam.set(cv2.CAP_PROP_FRAME_WIDTH , width)
my_cam.set(cv2.CAP_PROP_FRAME_HEIGHT , height)
my_cam.set(cv2.CAP_PROP_FPS , 30)
my_cam.set(cv2.CAP_PROP_FOURCC , cv2.VideoWriter_fourcc(*'MJPG'))
cv2.namedWindow('Tracker')
cv2.moveWindow('Tracker' , width , 0)

Hue_min = 10
Hue_max = 22
Hue_min2 = 163
Hue_max2 = 179
Sat_min = 69
Sat_max = 239
val_min = 124
val_max = 230
xpos =0
ypos =0
def callback1(val):
    global Hue_min
    Hue_min = val

def callback2(val):
    global Hue_max
    Hue_max = val

def callback3(val):
    global Sat_min
    Sat_min = val

def callback4(val):
    global Sat_max
    Sat_max = val

def callback5(val):
    global val_min
    val_min = val

def callback6(val):
    global val_max
    val_max = val

def callback7(val):
    global Hue_min2
    Hue_min2 = val

def callback8(val):
    global Hue_max2
    Hue_max2 = val



cv2.createTrackbar('Hue Min','Tracker' , 10 , 179 , callback1)
cv2.createTrackbar('Hue Max','Tracker' , 20 , 179 , callback2)
cv2.createTrackbar('Sat Min','Tracker' , 30 , 255 , callback3)
cv2.createTrackbar('Sat Max','Tracker' , 110 , 255 , callback4)
cv2.createTrackbar('Val Min','Tracker' , 40 , 255 , callback5)
cv2.createTrackbar('Val Max','Tracker' , 140 , 255 , callback6)
cv2.createTrackbar('Hue Min2','Tracker' , 10 , 179 , callback7)
cv2.createTrackbar('Hue Max2','Tracker' , 20 , 179 , callback8)




while True:
    x , frame = my_cam.read()
    frame_HSV = cv2.cvtColor(frame , cv2.COLOR_BGR2HSV)
    lower_bound = np.array([Hue_min , Sat_min , val_min])
    upper_bound = np.array([Hue_max , Sat_max , val_max])
    lower_bound2 = np.array([Hue_min2 , Sat_min , val_min])
    upper_bound2 = np.array([Hue_max2 , Sat_max , val_max])
    my_mask = cv2.inRange(frame_HSV , lower_bound , upper_bound)
    my_mask2 = cv2.inRange(frame_HSV , lower_bound2 , upper_bound2)
    my_mask_composite = cv2.add(my_mask , my_mask2)
    Object_of_intrest = cv2.bitwise_or(frame , frame,mask=my_mask_composite)
    Object_of_intrest_resize = cv2.resize(Object_of_intrest , (320 , 180))
    contours,flag = cv2.findContours(my_mask_composite , cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        area = cv2.contourArea(contour)
        if area >=100:
            #cv2.drawContours(frame , [contour] , 0 , (85,165 , 250),3)
            x1 , y1 , x2 , y2 = cv2.boundingRect(contour)
            cv2.rectangle(frame , (x1,y1) , (x1+x2 , y1+y2) , (0,255,255) , 3)
            xpos = int((x1/640)*1920)
            ypos = int((y1/360)*1080)
        
    
    
    
    
    
    
    cv2.imshow('My_cam' , frame)
    cv2.moveWindow('My_cam' , xpos,ypos)
    my_mask_comp_resize = cv2.resize(my_mask_composite , (320 , 180))
    cv2.imshow('My_mask' , my_mask_comp_resize)
    cv2.moveWindow('My_mask' , 0,height+140)
    cv2.imshow('OI' , Object_of_intrest_resize)
    cv2.moveWindow('OI' , 320,height+140)
    cv2.moveWindow('My_mask' , 0,height+140)

    if cv2.waitKey(100) & 0xff == ord('q'):
        break

my_cam.release()
