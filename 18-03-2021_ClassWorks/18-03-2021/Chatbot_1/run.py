import os
import playsound
import subprocess


while True:
	userdata = input("You: ")
	userdata = userdata.lower()

	if userdata == "hello":
		print("Hi")

	elif userdata == "what is your name":
		print("My name is Greenbot")
		user_name = input("What is  your name:- ")
		print(f"{user_name} is a nice name")

	elif userdata == "how are you":
		print("I am fine")
		user_ans = input("what about you: ")

		if user_ans == "i am ok":
			print("good!")
		elif user_ans == "i am bad":
			print("it will be ok, don't worry!")

	elif userdata == "song":
		print("")
		print("01.English Song")
		print("02.Mutta_Bhajji")
		print("03.Thalli_Pogathey")
		print("")

		songnumber = input("Enter the number of song: ")

		if songnumber == "1":
			playsound.playsound("English_song.mp3")

		elif songnumber == "2":
			playsound.playsound("Mutta_Bhajji.mp3")

		elif songnumber == "3":
			playsound.playsound("Thalli_Pogathey.mp3")

	elif userdata == "open this pc":
		os.system('explorer')

	elif userdata == "open notepad":
		os.system('notepad')

	elif userdata == "open cmd":
		os.system("cmd")

	elif userdata == "image":
		print("")
		print("01.dog image")
		print("02.cat image")
		print("03.lion image")
		print("")

		image_number = input("Enter the image number")

		if image_number == "1":
			os.system("dog.jpg")
		elif image_number == "2":
			os.system("cat.jpg")
		elif image_number == "3":
			os.system("lion.jpg")

	else:
		print("I don't know")