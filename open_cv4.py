import cv2
my_cam = cv2.VideoCapture(0)
rows = int(input('Dude , How many rows do you want?'))
cols = int(input('Dude , How many cols do you want?'))
std_width = 1280
std_height = 720

my_cam.set(cv2.CAP_PROP_FRAME_WIDTH ,std_width)
my_cam.set(cv2.CAP_PROP_FRAME_HEIGHT , std_height)
my_cam.set(cv2.CAP_PROP_FPS , 30)
my_cam.set(cv2.CAP_PROP_FOURCC , cv2.VideoWriter_fourcc(*'MJPG'))

while True:
    x , frame = my_cam.read()
    frame = cv2.resize(frame,(int(std_width/rows),int(std_height/cols)))
    for i in range(rows):

        for j in range(cols):
            
            cv2.imshow(f'{i}{j}',frame)
            cv2.moveWindow(f'{i}{j}',(std_width//rows)*i,((std_height//cols)*j)+30)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

my_cam.release()
