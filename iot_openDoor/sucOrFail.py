import boto3
import botocore
import face_recognition

import cv2
import time
import os
import datetime

detect_face_name=face_recognition.face_name

path = 'cctv/'
newCode="sudo modprobe bcm2835-v4l2"

#실패시 cctv 촬영
def Camera_cctv():
    camera = cv2.VideoCapture(0)

    # Define the codec and create VideoWriter object to save the video
    fourcc = cv2.VideoWriter_fourcc(*'XVID')

    video_writer = cv2.VideoWriter( 'output.avi', fourcc, 30.0, (640, 480))


    while True:

        (grabbed, frame) = camera.read()  # grab the current frame
        frame = cv2.resize(frame, (640,480))
        cv2.imshow("Frame", frame)  # show the frame to our screen
        key = cv2.waitKey(33) & 0xFF
        video_writer.write(frame)  # Write the video to the file system

         # I don't really have an idea what this does, but it works..
        if key == 27:
             break

    # cleanup the camera and close any open windows
    camera.release()
    video_writer.release()
    cv2.destroyAllWindows()
    print("\n\nBye bye\n")
    


def aws_face_send(detect_face_name)
	s3= boto3.client('s3') # s3객체생성

	# upload_file로 업로드하기

	#버킷이름
	bucket_name='face-images-storage'

	#인식 성공한 얼굴파일
	file_name='successCap/'+detect_face_name+'.png' 
	#s3에 png 파일 보내기
	s3.upload_file(file_name,bucket_name,detect_face_name+'.png',ExtraArgs={'ACL':'public-read', 'ContentType': 'image/png'})

	#인식 성공시점 로그 json 파일
	json_name='result/'+detect_face_name+'.json' 
	#s3에 json 파일 보내기
	s3.upload_file(json_name,bucket_name,detect_face_name+'.json',ExtraArgs={'ACL':'public-read', 'ContentType': 'application/json'})

	#detect_face_name+'.png'/ detect_face_name+'.json' 파일이 버킷에 올라갈 이름

	# 버킷 이름 모두 출력
	response = s3.list_buckets()
	buckets = [bucket['Name'] for bucket in response['Buckets']]
	print("Bucket List: %s 에 저장되었습니다" % buckets)
	
	
aws_face_send(detect_face_name)




