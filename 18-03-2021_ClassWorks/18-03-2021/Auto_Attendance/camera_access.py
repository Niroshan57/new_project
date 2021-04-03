import cv2 #opencv
from pyzbar.pyzbar import decode
from PIL import Image
import playsound

cap = cv2.VideoCapture(0)

while True:
	ret, frame = cap.read()
	#img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	cv2.imshow("Display", frame)
	#cv2.imshow("gray",img_gray)
	cv2.imwrite("cache_img.jpg",frame)

	data = decode(Image.open('cache_img.jpg'))

	if len(data) > 0:
		data = decode(Image.open('cache_img.jpg'))
		qr_data = data[0][0].decode('utf-8')

		if qr_data == "guna123":
			playsound.playsound("song.mp3")

			


	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()





