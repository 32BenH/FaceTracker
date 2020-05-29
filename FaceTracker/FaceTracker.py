import cv2
import numpy as np

capture = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier('faces.xml')

while True:
	#Captures a frame
	ret, frame = capture.read()
	
	#Find the faces
	faces = faceCascade.detectMultiScale(frame, 1.3, 5)

	#Draw the rectangle around the faces
	for (x, y, w, h) in faces:
		cv2.rectangle(frame, (x, y), (x+w, y+h), (255,0,0), 2)

	#Displays the frame
	cv2.imshow('Camera', frame)

	#Break if q is pressed
	if cv2.waitKey(1) & 0xFF == 27:
		break

capture.release()
cv2.destroyAllWindows()
