import cv2

faceModel = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eyeModel = cv2.CascadeClassifier("haarcascade_eye.xml")


cap=cv2.VideoCapture(0)

while True:
	ret,frame = cap.read()

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = faceModel.detectMultiScale(gray,1.3,5)

	for (x,y,w,h) in faces:
		graySection = gray[y:y+h, x:x+w]
		frameSection = frame[y:y+h, x:x+w]
		cv2.rectangle(frame, (x,y), (x+w,y+h),(0,255,0),2)

		cv2.putText(frame,"Face Detected", (x+w, y+h),cv2.FONT_HERSHEY_SIMPLEX ,0.5,(0,0,255),1,cv2.LINE_AA)

		eyes = eyeModel.detectMultiScale(graySection)
		cv2.imshow("RGB", frameSection)

		

		for (ex,ey,ew,eh) in eyes:
			cv2.rectangle(frameSection,(ex,ey),(ex+ew,ey+eh),(0,255,0),1)
		

	cv2.imshow("Display",frame)

	

	if cv2.waitKey(1) & 0xFF == ord("q"):
		break


cap.release()
cv2.destroyAllWindows()