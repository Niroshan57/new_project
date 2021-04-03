import cv2
from pyzbar.pyzbar import decode
from PIL import Image


cap=cv2.VideoCapture(0)

while True:
	ret, frame=cap.read()

	cv2.imshow("display",frame)
	cv2.imwrite("cache img.jpg",frame)


	if len(data)>0:
		data=decode(Image.open("cache img.jpg"))


	print(data[0][0].decode("utf-8"))


	if cv2.waitKey(1) & 0xFF == ord("q"):
		break


cap.release()
cv2.destroyAllWindows()
