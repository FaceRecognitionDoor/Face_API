#!/opt/local/bin/python
# -*- coding: utf-8 -*-
import cv2
CAM_ID = 0

#Open the CAM
cap = cv2.VideoCapture(CAM_ID) #ī�޶� ����

#Check that the camera is opened
if cap.isOpened() == False: #ī�޶� ���� Ȯ��
    print ('Can\'t open the CAM(%d)' % (CAM_ID))
    exit()

#create the window & change the window size
#������ ���� �� ������ ����
cv2.namedWindow('Face')

face_cascade = cv2.CascadeClassifier()
face_cascade.load('C:/opencv/build/etc/haarcascades/haarcascade_frontalface_default.xml')


while(True):
    #read the camera image
    #ī�޶󿡼� �̹��� ���
    ret, frame = cap.read()

    grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    grayframe = cv2.equalizeHist(grayframe)

    faces = face_cascade.detectMultiScale(grayframe, 1.1, 3, 0, (30, 30))
   
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3, 4, 0)
    
    cv2.imshow('Face',frame)

    #wait keyboard input until 10ms
    #10ms ���� Ű�Է� ���
    if cv2.waitKey(10) >= 0:
        break;

#close the window
#������ ����
cap.release()
cv2.destroyWindow('Face')