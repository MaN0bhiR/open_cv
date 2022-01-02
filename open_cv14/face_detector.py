import cv2
import time



width = 640
height = 360
INI_FPS = 30
fpsstr = '30'
my_cam = cv2.VideoCapture(0)

my_cam.set(cv2.CAP_PROP_FRAME_WIDTH , width)
my_cam.set(cv2.CAP_PROP_FRAME_HEIGHT , height)
my_cam.set(cv2.CAP_PROP_FPS , 30)
my_cam.set(cv2.CAP_PROP_FOURCC , cv2.VideoWriter_fourcc(*'MJPG'))

face_cascade = cv2.CascadeClassifier('haar/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haar/haarcascade_eye.xml')

while True:
    start = time.time()
    x , frame = my_cam.read()
    gray_frame = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_frame , 1.3 ,5)
    eyes = eye_cascade.detectMultiScale(gray_frame,1.3,5)
    
    for face in faces:
        x,y,w,h = face
        cv2.rectangle(frame , (x,y), (x+w,y+h),[0,255,0],3)
    
    for eye in eyes:
        x,y,w,h = eye
        cv2.rectangle(frame , (x,y), (x+w,y+h),[0,0,255],3)
    cv2.putText(frame,fpsstr ,(450,100),cv2.FONT_HERSHEY_COMPLEX,1,(60,168,200),1 )
    cv2.imshow('My_cam' , frame)


    if cv2.waitKey(100) & 0xff == ord('q'):
        break

    stop = time.time()
    duration = start - stop

    IFPS = 1//duration
    FPS = (0.5*INI_FPS) + (0.5*IFPS)
    
    fpsstr = str(round(FPS , 1)) + "FPS"
    print(FPS)

my_cam.release()
