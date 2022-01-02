import cv2
import face_recognition as fr
from face_recognition import load_image_file

font = cv2.FONT_HERSHEY_COMPLEX

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


Unknown_face = load_image_file('demo_imgs/demoImages-master/unknown/u5.jpg')
Unknown_face_BGR = cv2.cvtColor(Unknown_face , cv2.COLOR_RGB2BGR)
Uface_loc = fr.face_locations(Unknown_face)
Uface_encode = fr.face_encodings(Unknown_face)

for location , encoding in zip(Uface_loc , Uface_encode):
    t, r , b, l = location
    print(location)
    cv2.rectangle(Unknown_face_BGR , (l,t),(r,b),(0,255,255),2)
    name = 'Unknown_person'
    matches = fr.compare_faces(knownEncodings , encoding)
    print(matches)
    
    if True in matches:
        matchIndex = matches.index(True)
        pre_name = names[matchIndex]
        print(names[matchIndex])
        cv2.putText(Unknown_face_BGR , pre_name ,(l,t) ,font,2,(0,255,0),3)
    


cv2.imshow('Photo',Unknown_face_BGR)
cv2.waitKey(100000)
 