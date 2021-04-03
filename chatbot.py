import playsound
import subprocess

while True:
	userdata = input()
	userdata = userdata.lower()
	
	if userdata == "hi":
		print("hello, how can i help you")

	elif userdata == "what is your name":
		print("my name is Stella")
		username= input("what is your name")
		print("wow! nice name")

	elif userdata == "how are you":
		print("I'm petty good")
		userAns = input("what about you")


	elif userdata=="song":
		print("")
		print("01 Yaro ivan")
		print("02 Velicha poove vaa")

		songNum = input("enter the song number: ")

		if songNum == "1":
			playsound.playsound("1.mp3")
		elif songNum == "2":
			playsound.playsound("2.mp3")

	elif userdata == "open this pc":
			subprocess.Popen("explorer")

	elif userdata == "open notepad":
			subprocess.Popen("notepad")


