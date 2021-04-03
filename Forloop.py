alphabet = ["a", "b", "c" "d"]

founded = False

for x in alphabet:
	if x == "e":
		founded = True
		break

	else:
		founded = False

	if founded == False:
		print ("Not founded")

	elif founded == True:
		print ("Founded")