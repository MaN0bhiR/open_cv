'''import cv2
import face_recognition as fr

import numpy as np

Classifier = cv2.CascadeClassifier('haar/haarcascade_frontalface_default.xml')
my_photo = fr.load_image_file('demo_imgs/demoImages-master/known/Photo-6.jpeg')
face_loc = fr.face_locations(my_photo)
my_face_encodings = fr.face_encodings(my_photo)

names = ['Abhi']

MikeFace = fr.load_image_file('demo_imgs/demoImages-master/known/Mike Pence.jpg')
face_loc = fr.face_locations(MikeFace)[0]
MikeFaceEncode = fr.face_encodings(MikeFace)[0]

known_encodings = [my_face_encodings]
#names.append('Mike Pence')

width = 640
height = 360
my_cam = cv2.VideoCapture(0)

my_cam.set(cv2.CAP_PROP_FRAME_WIDTH , width)
my_cam.set(cv2.CAP_PROP_FRAME_HEIGHT , height)
my_cam.set(cv2.CAP_PROP_FPS , 30)
my_cam.set(cv2.CAP_PROP_FOURCC , cv2.VideoWriter_fourcc(*'MJPG'))

while True:
    x , frame = my_cam.read()
    
    
    gray_scale = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
    RCB_scale = cv2.cvtColor(frame , cv2.COLOR_BGR2RGB)
    face_loca = fr.face_locations(gray_scale)
    face_enocod = fr.face_encodings(frame)
    
    
    for encoding ,locations in zip(face_enocod,face_loca):
        print(locations)
        t , r , b , l = locations
        cv2.rectangle(frame , (l ,t),(r,b),(0,255,255),2 )
        matches = fr.compare_faces(known_encodings , encoding)
        matches = np.array(matches[0])
        print(matches)
        for match in matches:
            if match == True:
                match_index = matches.index(match)
                name = names[match_index]
                cv2.putText(frame , name , (l,t) , cv2.FONT_HERSHEY_COMPLEX , 2 , (0,127 , 140) , 3)


    
    
    

    
    
    cv2.imshow('My_cam' , frame)
    if cv2.waitKey(100) & 0xff == ord('q'):
        break

my_cam.release()
'''




import cv2
import face_recognition as fr
from face_recognition import load_image_file

font = cv2.FONT_HERSHEY_COMPLEX
width = 640
height = 360
my_cam = cv2.VideoCapture(0)

my_cam.set(cv2.CAP_PROP_FRAME_WIDTH , width)
my_cam.set(cv2.CAP_PROP_FRAME_HEIGHT , height)
my_cam.set(cv2.CAP_PROP_FPS , 30)
my_cam.set(cv2.CAP_PROP_FOURCC , cv2.VideoWriter_fourcc(*'MJPG'))

donFace = load_image_file('demo_imgs/demoImages-master/known/Donald Trump.jpg')
face_loc = fr.face_locations(donFace)[0]
donFaceEncode = fr.face_encodings(donFace)[0]

AntFace =load_image_file('demo_imgs/demoImages-master/known/Anthony Fauci.jpg')
face_loc = fr.face_locations(AntFace)[0]
AntFaceEncode = fr.face_encodings(AntFace)[0]
 
BillFace =load_image_file('demo_imgs/demoImages-master/known/Anthony Fauci.jpg')
face_loc = fr.face_locations(BillFace)[0]
BillFaceEncode = fr.face_encodings(BillFace)[0]
knownEncodings = [donFaceEncode , AntFaceEncode , BillFaceEncode]
names = ['Donald Trump' , 'Anthony Fauci' , 'Bill Barr']

MikeFace = load_image_file('demo_imgs/demoImages-master/known/Mike Pence.jpg')
face_loc = fr.face_locations(MikeFace)[0]
MikeFaceEncode = fr.face_encodings(MikeFace)[0]

knownEncodings.append(MikeFaceEncode)
names.append('Mike Pence')

AbhiFace = load_image_file('demo_imgs/demoImages-master/known/Photo-6.jpeg')
face_loc = fr.face_locations(AbhiFace)[0]
AbhiFaceEncode = fr.face_encodings(AbhiFace)[0]

knownEncodings.append(AbhiFaceEncode)
names.append('Abhi')

while True:
    x , frame = my_cam.read()
    
    

    Unknown_face = frame
    
    Uface_loc = fr.face_locations(Unknown_face)
    Uface_encode = fr.face_encodings(Unknown_face)

    for location , encoding in zip(Uface_loc , Uface_encode):
        t, r , b, l = location
        print(location)
        cv2.rectangle(Unknown_face , (l,t),(r,b),(0,255,255),2)
        name = 'Unknown_person'
        matches = fr.compare_faces(knownEncodings , encoding)
        print(matches)
        
        if True in matches:
            matchIndex = matches.index(True)
            pre_name = names[matchIndex]
            print(names[matchIndex])
            cv2.putText(Unknown_face, pre_name ,(l,t) ,font,2,(0,255,0),3)
        

        cv2.imshow('My_cam' , frame)
        if cv2.waitKey(100) & 0xff == ord('q'):
                break
        
my_cam.release()