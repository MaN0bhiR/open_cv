import cv2

my_cam = cv2.VideoCapture(0)

while True:
    x , frame = my_cam.read()
    black_white_frame = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
    cv2.imshow('colour_frame_1' , frame)
    cv2.moveWindow('colour_frame_1' , 0 ,0)
    cv2.imshow('Grey_frame_1' , black_white_frame)
    cv2.moveWindow('Grey_frame_1' , 4000 ,0)
    cv2.imshow('Grey_frame_2' , black_white_frame)
    cv2.moveWindow('Grey_frame_2' , 0 ,550)
    cv2.imshow('colour_frame_2' , frame)
    cv2.moveWindow('colour_frame_2' , 4000 ,550)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

my_cam.release()