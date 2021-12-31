import cv2
print(cv2.__version__)
Integrated_cam = cv2.VideoCapture(0)
while True:
    c , frame = Integrated_cam.read()
    cv2.imshow('My_cam' , frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
Integrated_cam.release()
