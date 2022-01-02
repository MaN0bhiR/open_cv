import cv2
import os
import face_recognition as fr
import pickle


image_dir = '/home/abhi/open_cv/demo_imgs/demoImages-master/unknown'
with open('train.pkl' , 'rb') as f:
    known_names = pickle.load(f)
    known_encodings = pickle.load(f)

print(known_names)
for root , dirs , files in os.walk(image_dir):
    for file in files:
        path = os.path.join(root , file)
        Unknown_img = fr.load_image_file(path)
        Fac_loc = fr.face_locations(Unknown_img)
        Unknown_encoding = fr.face_encodings(Unknown_img)
        
        
        
        for loaction ,encoding in zip(Fac_loc,Unknown_encoding):
            t,r,b,l = loaction
        
            cv2.rectangle(Unknown_img , (l,t) , (r,b)  ,(0,127 , 250) , 3 )
            mathces = fr.compare_faces(known_encodings , encoding)
           

            if True in mathces:
                matchIndex = mathces.index(True)
                name = known_names[matchIndex]
                cv2.putText(Unknown_img , name , (l,t) , cv2.FONT_HERSHEY_COMPLEX , 1 , (127 , 145  , 240) , 1)
        Unknown_img = cv2.cvtColor(Unknown_img , cv2.COLOR_RGB2BGR)        
        cv2.imshow('name' , Unknown_img)
        cv2.waitKey(6000)   
                