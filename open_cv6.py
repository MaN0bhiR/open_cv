import cv2
import time
width = 1280
Height = 720
my_cam = cv2.VideoCapture(0)
my_cam.set(cv2.CAP_PROP_FRAME_WIDTH ,width )
my_cam.set(cv2.CAP_PROP_FRAME_HEIGHT ,Height )
my_cam.set(cv2.CAP_PROP_FOURCC , cv2.VideoWriter_fourcc(*'MJPG'))
INI_FPS=30
my_cam.set(cv2.CAP_PROP_FPS , INI_FPS)
fpsstr = '30'
while True:
    start = time.time()
    x , frame = my_cam.read()
    cv2.rectangle(frame ,(1125,35), (1265,70) , (0,0,0) , -4 )
    cv2.putText(frame,fpsstr ,(1130,65),cv2.FONT_HERSHEY_COMPLEX,1,(60,168,200),2 )
    
    cv2.imshow('MY_CAM', frame)

    if cv2.waitKey(1)&0xff == ord('q'):
        break

    stop = time.time()
    duration = stop-start
    

    IFPS = 1//duration
    FPS = (0.5*INI_FPS) + (0.5*IFPS)
    
    fpsstr = str(round(FPS , 1)) + "FPS"
    print(FPS)

my_cam.release()