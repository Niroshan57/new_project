import cv2

faceModel = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eyeModel = cv2.CascadeClassifier("haarcascade_eye.xml")

Cam = cv2.VideoCapture(0)

while True:

	r,frame = Cam.read()

	grayFace = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	ColorFace = faceModel.detectMultiScale(grayFace,1.3,5)

	for (a,b,c,d) in ColorFace:
		sectionGray = grayFace [a:a+c, b:b+d]
		sectionColor = ColorFace[a:a+c, b:b+d]

		cv2.rectangle(frame, (a,b), (a+c,b+d),(0,255,0),2)

		eye = eyeModel.detectMultiScale(sectionGray)

		for (ea,eb,ec,ed) in eye:
			cv2.rectangle(sectionColor, (ea,eb),(ea+ec, eb+ed),(0,0,255),2)


	cv2.imshow("Camera", frame)

	if cv2.waitKey(1) & 0xFF == ("q"):
		break

Cam.release()
cv2.destroyAllWindows()


