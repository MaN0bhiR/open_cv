import os
import cv2
import face_recognition as fr
import pickle

img_dir = '/home/abhi/open_cv/demo_imgs/demoImages-master/known'
known_encodings = []
names = []
for root , dirs  , files in os.walk(img_dir):
    
    for file in files:
        src_path = os.path.join(root,file) 
        
        name = os.path.splitext(file)[0]
        photo = fr.load_image_file(src_path)
        photo_encodings = fr.face_encodings(photo)[0]
        known_encodings.append(photo_encodings)
        names.append(name)

def Known_encodings_and_names():
    return known_encodings,names

with open('train.pkl' , 'wb') as f:
    pickle.dump(names , f)
    pickle.dump(known_encodings,f)



