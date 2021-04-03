import playsound
import subprocess
import os

while True:
	userdata = input("you:")
	userdata = userdata.lower()
	
	if userdata == "hi":
		print("hello, how can i help you")

	elif userdata == "what is your name":
		print("my name is Stella")
		userAns = input("what is your name: ")

		print(f"{userAns} nice name")

	elif userdata == "how are you":
		print("I'm petty good")
		userAns = input("what about you: ")

	elif userdata == "how old are you":
		print("i was launched in 2021.03.18, so technically i'm pretty young")

	elif userdata == "add":
		print("sure i can")

		n = int(input("enter number: "))
		sum = 0
		for n in range(1,n+1,1):
			sum=sum+n
		print("total is ", sum)




	elif userdata == "song":
		print("")
		print("01 Yaro ivan")
		print("02 Velicha poove vaa")

		songNum = input("enter the song number: ")

		if songNum == "1":
			playsound.playsound("yaaro.mp3")
		elif songNum == "2":
			playsound.playsound("velicha.mp3")



	elif userdata == "open this pc":
		subprocess.Popen("explorer")

	elif userdata == "open notepad":
		subpocess.Popen("notepad")


	elif userdata == "image":
		print("")
		print ("image 1 mask")
		print ("image 2 blood")

		imageNum = input ("enter the image number")

		if imageNum == "1":
			os.system("mask.jpg")

		elif imageNum == "2":
			os.system("blood.png")