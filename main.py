import cv2
import numpy as np
import face_recognition
import os
###  from datetime import datetime
import serial                                    #NLI
import time                                      #NLI
ser=serial.Serial('COM5',9600)                   #NLI
ser.timeout=1                                    #NLI
def mark_attendance(name):
    ser.write(name.encode())                     #NLI
    time.sleep(0.5)                              #NLI
    #if True:
      #attendance_file=open('attendance.csv', 'r+')
      #att_list = attendance_file.readlines()
      #present_list = []
      #for data in att_list:
        #entry = data.split(',')
        #present_list.append(entry[0])
      #if name not in present_list:
        #now = datetime.now()
        #date_time = now.strftime('%H:%M:%S')
        #attendance_file.writelines(f'\n{name},{date_time}')


path='D:\known_faces'
known_images=[]
encoded_images=[]
path=os.path.join(path)
print(os.listdir(path))
for img in os.listdir(path):
#    img = cv2.imread(path+'/'+img)
    img=face_recognition.load_image_file(f'{path}/{img}')
    known_images.append(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_enc = face_recognition.face_encodings(img)
    encoded_images.append(img_enc)
# print(len(encoded_images))
# print(type(encoded_images))
# print(type(encoded_images[0]))
#
# print(type(encoded_images[0][0]))
#
# print(encoded_images[0][0].shape)


live_video=cv2.VideoCapture(0,cv2.CAP_DSHOW)#,cv2.CAP_DSHOW
 #while (live_video.isOpened()):
while True:

    frame_confirm, live_frame =live_video.read()
 #   frame=cv2.resize(frame1,(0,0),None,0.25,0.25)
    frame=cv2.cvtColor(live_frame,cv2.COLOR_BGR2RGB)

    frame_locations=face_recognition.face_locations(frame)
    frame_encodings=face_recognition.face_encodings(frame,frame_locations)
 #   for i in range(0,len(encoded_images)):
    for f_encode,f_location in zip(frame_encodings,frame_locations):
          # print(type(f_encode))
          # print(f_encode.shape)
          # print('dhdhhdhdhd')
          # print(type(encoded_images[0]))
          # print(len(encoded_images[0]))
  #       match=face_recognition.compare_faces([encoded_images[0][0]][0],[f_encode][0])
      dist_list=[]
      for i in range(0,len(encoded_images)):
        match_dist=face_recognition.face_distance(encoded_images[i],f_encode)
        dist_list.append(match_dist)
      #  print(i)
        # print(type(match_dist))
        # print(match_dist.shape)
      #  print(match_dist)
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
     # live_frame=cv2.resize(live_frame,(580,440))
      cv2.imshow('cam', live_frame)
      cv2.waitKey(1)
          # list=[]
          # if(i<len(encoded_images)-1):
          #     list.append(match_dist)
          # elif(i==len(encoded_images)-1):
          #     list.append(match_dist)
          #     print(list)





