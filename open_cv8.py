import cv2
import numpy
click = 0

def mouseclick(event , x , y , para , para2):
    global click 
    global x1 , x2 , y1 , y2
    
    
    
    
    if click >2:
            x1 , x2 , y1 , y2 , click = x,y,0,0,1
    if  event == 1:
        if click%2==0:
            x1 = x
            y1 = y 
            click+=1
            print(click)
        
        elif click%2!=0:
            x2 = x
            y2 = y 
            click+=1
            print(click)
        
    
    
    
    
    
width = 1280
height = 720
my_cam = cv2.VideoCapture(0)

my_cam.set(cv2.CAP_PROP_FRAME_WIDTH , width)
my_cam.set(cv2.CAP_PROP_FRAME_HEIGHT , height)
my_cam.set(cv2.CAP_PROP_FPS , 30)
my_cam.set(cv2.CAP_PROP_FOURCC , cv2.VideoWriter_fourcc(*'MJPG'))
cv2.namedWindow('My_cam')
cv2.setMouseCallback('My_cam' , mouseclick)

while True:
    x , frame = my_cam.read()
    cv2.imshow('My_cam' , frame)
    cv2.moveWindow('My_cam' , 0,0)
    if click ==2:

    
        point1 = (x1 , y1)
        point2 = (x2 , y2)
        ROI_frame = frame[y1:y2,x1:x2]
        cv2.imshow('ROI_FRAME' , ROI_frame)
        cv2.moveWindow('ROI_FRAME' , 1300 , 750)
        
    


    
    
    
    if cv2.waitKey(100) & 0xff == ord('q'):
        break

my_cam.release()

