import cv2
import numpy as np
while True:
    frame = np.zeros([64,64,3],dtype=np.uint8)
    for i in range(8):
        for j in range(8):
            if i%2 !=0 and j%2 !=0:
                frame[(i*8):((i+1)*8),(j*8):((j+1)*8)]=(0,0,0)
            elif i%2 !=0:
                frame[(i*8):((i+1)*8),(j*8):((j+1)*8)]=(0,0,255)
            elif j%2 !=0:
                frame[(i*8):((i+1)*8),(j*8):((j+1)*8)]=(0,0,255)
            if i%2 !=0 & j%2 !=0:
                frame[(i*8):((i+1)*8),(j*8):((j+1)*8)]=(0,0,255)
    frame1 = np.array(cv2.resize(frame , (640,640)))
    cv2.imshow('Checker_board'  , frame1)
    if cv2.waitKey(1)& 0xff == ord('q'):
        break