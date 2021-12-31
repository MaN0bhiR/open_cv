import cv2
import numpy
width = 256
height = 720
while True:
    frame = numpy.zeros([width,height,3],dtype=numpy.uint8)
    frame = cv2.cvtColor(frame , cv2.COLOR_BGR2HSV)
    frame1 = numpy.zeros([width,height,3],dtype=numpy.uint8)
    frame1 = cv2.cvtColor(frame1 , cv2.COLOR_BGR2HSV)
    for hue in range(720):
        for sat in range(256):
            frame[sat][hue] = (int(hue/4),sat , 255)
            frame1[sat][hue] = (int(hue/4),255 , sat)

    frame = cv2.cvtColor(frame , cv2.COLOR_HSV2BGR)
    frame1 = cv2.cvtColor(frame1 , cv2.COLOR_HSV2BGR)
    cv2.imshow('MY_frame' , frame)
    cv2.moveWindow('MY_frame' , 0 ,0)
    cv2.imshow('MY_frame1' , frame1)
    cv2.moveWindow('MY_frame' , 0 ,256)

    if cv2.waitKey(1) &0xff == ord('q'):
        break



