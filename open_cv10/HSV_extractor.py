import cv2
import numpy

evt =0


width = 640
height = 360
my_cam = cv2.VideoCapture(0)

my_cam.set(cv2.CAP_PROP_FRAME_WIDTH , width)
my_cam.set(cv2.CAP_PROP_FRAME_HEIGHT , height)
my_cam.set(cv2.CAP_PROP_FPS , 30)
my_cam.set(cv2.CAP_PROP_FOURCC , cv2.VideoWriter_fourcc(*'MJPG'))
cv2.namedWindow('My_cam')
def mousecallback(event , x , y , flags , para):
    global evt
    global point
    evt = event
    point = (x,y)
cv2.setMouseCallback('My_cam' , mousecallback)

while True:
    x , frame = my_cam.read()
    HSV_frame = cv2.cvtColor(frame , cv2.COLOR_BGR2HSV)
    cv2.imshow('My_cam' , frame)
    cv2.moveWindow('My_cam' , 0 ,0)

    if evt == 1 or evt ==4:
        png = numpy.zeros([180 ,320,3],dtype=numpy.uint8)
        clr = (HSV_frame[point[1]][point[0]])
        print(clr)
        png[:]=clr
        cv2.putText(png , str(clr) , [50 ,50] , cv2.FONT_HERSHEY_COMPLEX , 1 , (68,127 ,200 ), 1)
        cv2.imshow('Color' , png)
        
        evt = 0

    if cv2.waitKey(100) & 0xff == ord('q'):
        break

my_cam.release()
