import cv2
import numpy
width = 160
height = 90
my_cam = cv2.VideoCapture(0)
my_cam.set(cv2.CAP_PROP_FOURCC , cv2.VideoWriter_fourcc(*('MJPG')))
my_cam.set(cv2.CAP_PROP_FPS ,30)
w =0
h=0
def width1(len):
    global w
    global h
    if len>0:
        
        w = len*160
        h= len*90
    else:
        w = 160
        h = 90


        


my_cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
my_cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)


cv2.namedWindow('My_track_bar')
cv2.createTrackbar('width' , 'My_track_bar' , 1 , 8 , width1)

cv2.moveWindow('My_track_bar',1930,1090)



while True:
    my_cam.set(cv2.CAP_PROP_FRAME_WIDTH,w)
    my_cam.set(cv2.CAP_PROP_FRAME_HEIGHT,h)
    x , focus = my_cam.read()
    cv2.imshow('My_cam' , focus)
    cv2.moveWindow('My_cam', 0 , 0)
    print("width = " , w)
    print("height = " , h)
    if cv2.waitKey(1)&0xff == ord('q'):
        break


my_cam.release()
