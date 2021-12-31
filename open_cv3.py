import cv2

width = 160
height = 90
my_cam = cv2.VideoCapture(0)

my_cam.set(cv2.CAP_PROP_FRAME_WIDTH , width)
my_cam.set(cv2.CAP_PROP_FRAME_HEIGHT , height)
my_cam.set(cv2.CAP_PROP_FPS , 30)
my_cam.set(cv2.CAP_PROP_FOURCC , cv2.VideoWriter_fourcc(*'MJPG'))

while True:
    x , frame = my_cam.read()
    cv2.imshow('My_cam' , frame)
    if cv2.waitKey(100) & 0xff == ord('q'):
        break

my_cam.release()
