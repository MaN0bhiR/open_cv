import cv2

width = 1280
height =720
c_x  = 640
c_y = 360
c_width = 125
c_height = 100
d_width = 20
d_height = 20


my_cam = cv2.VideoCapture(0)

my_cam.set(cv2.CAP_PROP_FRAME_WIDTH , width)
my_cam.set(cv2.CAP_PROP_FRAME_HEIGHT , height)
my_cam.set(cv2.CAP_PROP_FPS , 30)
my_cam.set(cv2.CAP_PROP_FOURCC , cv2.VideoWriter_fourcc(*'MJPG'))

while True:
    x , frame = my_cam.read()
    G_frame = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
    BGR_G_frame = cv2.cvtColor(G_frame , cv2.COLOR_GRAY2BGR)
    ROI_in = frame[int(c_y-c_height):int(c_y+c_height),int(c_x-c_width):int(c_x+c_width)]
    BGR_G_frame[int(c_y-c_height):int(c_y+c_height),int(c_x-c_width):int(c_x+c_width)]= ROI_in
    c_x = c_x-d_width
    c_y = c_y-d_height

    if c_y-c_height <=0 or c_y+c_height >= 720 :
        d_height = -(d_height)
    if c_x-c_width <=0 or c_x+c_width >= 1280:
        d_width = -(d_width)

    cv2.imshow('my_frame' ,BGR_G_frame)
    cv2.moveWindow('my_frame' , 0,0)

    if cv2.waitKey(100) & 0xff == ord('q'):
        break

my_cam.release()
