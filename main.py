import cv2
import numpy as np
import face_recognition
import os
import serial                                    
import time                                      
ser=serial.Serial('COM5',9600)                   
ser.timeout=1                                    
def mark_attendance(name):
    ser.write(name.encode())                     
    time.sleep(0.5)                              

path='D:\known_faces'
known_images=[]
encoded_images=[]
path=os.path.join(path)
print(os.listdir(path))
for img in os.listdir(path):
    img=face_recognition.load_image_file(f'{path}/{img}')
    known_images.append(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_enc = face_recognition.face_encodings(img)
    encoded_images.append(img_enc)


live_video=cv2.VideoCapture(0,cv2.CAP_DSHOW)
while True:

    frame_confirm, live_frame =live_video.read()
    frame=cv2.cvtColor(live_frame,cv2.COLOR_BGR2RGB)

    frame_locations=face_recognition.face_locations(frame)
    frame_encodings=face_recognition.face_encodings(frame,frame_locations)
    for f_encode,f_location in zip(frame_encodings,frame_locations):
       
      dist_list=[]
      for i in range(0,len(encoded_images)):
        match_dist=face_recognition.face_distance(encoded_images[i],f_encode)
        dist_list.append(match_dist)

      print(dist_list)
      index=np.argmin(dist_list)
      print(index)
      if(dist_list[index]<0.5):
        name=os.listdir(path)[index]
        name=name[0:8]
        print(name)
        cv2.rectangle(live_frame, (f_location[3], f_location[0]), (f_location[1], f_location[2]), (0, 255, 0), 2)
        cv2.rectangle(live_frame, (f_location[3], f_location[2]), (f_location[1], f_location[2] + 40), (0, 255, 0),cv2.FILLED)
        cv2.putText(live_frame, name, (f_location[3] + 15, f_location[2] + 15), cv2.FONT_HERSHEY_COMPLEX, 0.8,(0, 0 ,0), 2)
        mark_attendance(name)
      elif(dist_list[index]>=0.5):
        cv2.rectangle(live_frame, (f_location[3], f_location[0]), (f_location[1], f_location[2]), (0, 0, 255), 2)
        cv2.rectangle(live_frame, (f_location[3], f_location[2]), (f_location[1], f_location[2]+40), (0, 0, 255), cv2.FILLED)
        cv2.putText(live_frame,'Unknown',(f_location[3]+15, f_location[2]+15),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
      cv2.imshow('cam', live_frame)
      cv2.waitKey(1)
         





