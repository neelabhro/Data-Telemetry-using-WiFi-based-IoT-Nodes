import cv2
import time 
capture = cv2.VideoCapture(0)
i=0
while True:
	stime = time.time()
	ret, frame = capture.read()
	print(ret);
	#print(frame.widhth)
	#cv2.imshow('frame', frame)
	i = i+1
	time.sleep(1)
	cv2.imwrite("send/"+str(i)+".jpg",frame)
cv2.destroyAllWindows()
capture.release()
