print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to the Treasure Island. Your mission is to acquire the treasure!")

while True:
	direction = input("You are at the start of a double path, do you go right or left? ")
	if direction == 'right':
		go_or_stay = input("You are now in front of a quite large pond. Do you swim or wait for the boat? ")
		if go_or_stay == 'wait':
			which_door = input("You safely arrived at shore and saw a shackle.\nActually, the door is only one...\nBut you see different pills on a table.\nA red one and a blue one; besides a glass of pure water.\nDepending on your choice, the door will lead you to a different path: ")
			if which_door == 'red':
				print("Congratulations on your bravery, you are a true Gryffindor and chose the pill that lead you to the truth and you are now stronger than ever!")
				print('''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣤⣤⣶⣶⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣶⣦⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⡟⠛⠋⠉⠉⣹⡍⠁⠀⠀⠀⢠⣿⡇⣶⣶⣶⣶⣾⣿⣿⣿⣭⣽⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣷⡄⠀⠀⢰⣿⣿⠄⠀⠤⣤⣭⣟⣡⣽⣻⣿⣿⣿⣿⡟⠈⣿⣿⣿⢹⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣄⢠⣿⢿⣋⣾⣿⣿⣿⣿⣿⣿⠛⠿⠊⠻⢿⣿⣿⣶⣿⣿⣿⣏⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⠃⠀⠵⣿⣿⣿⣿⣿⣿⠿⠓⠀⠀⠀⠤⣤⠄⠉⠛⢻⣿⣿⣿⣿⡜⣿⣿⣿⣿⣦⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣦⣤⣤⣴⣾⣿⣿⣿⣿⣿⣿⠃⠀⠀⣾⣿⣿⣿⣿⣿⠠⠶⠆⠀⠀⠀⠀⠀⠀⠀⠀⠉⣿⣿⣿⣿⣿⣜⢿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠈⠃⠀⠀⠼⣿⣿⣿⣿⣿⣿⣦⣄⣀⠀⠀⠀⠀⣴⣷⣶⣶⣴⣿⣿⣿⣿⣿⣿⠗⠀⠀⠈⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢸⣿⣿⣿⣿⡿⢿⡟⠋⠀⠀⠀⣴⡀⢀⠾⣻⣿⣿⣿⣿⣿⣿⣿⣷⡆⠀⠀⠀⠻⠿⠿⠿⣿⣏⠀⣹⣿⣿⠇⠀⠀⠀⢰⣶⡎⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢸⣿⣿⣿⣿⠀⣾⣿⣄⠀⠀⣼⣿⣿⢄⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⣿⣿⣷⣿⣿⣿⡄⠀⠀⠀⣿⣿⡇⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢸⣿⣿⣿⣿⣾⣿⣿⣿⠆⠸⣿⣏⡵⠿⡻⣿⡿⣻⣿⣿⣿⣿⠋⢿⣿⣿⣷⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⣰⣿⣿⡇⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠸⣿⣿⣿⣿⡏⣿⣿⡏⠀⠀⠙⣿⡿⠃⠀⠘⢱⣿⣿⣿⣿⠃⠀⠀⠻⢿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠀⠀⢠⣿⣿⣿⣿⡇⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣿⣿⣿⠟⠉⠈⠙⠢⣄⠀⠀⠈⠁⠀⠀⠀⠘⢸⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠙⠻⠿⠿⢿⣿⡿⠃⠀⠀⠀⣸⣿⣿⢿⣿⡇⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀⢀⣤⠒⢄⠑⢄⣼⣦⠀⠀⠀⢠⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⡇⠀⠀⠀⢀⣿⣿⡁⢈⣿⡇⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢹⣿⡄⠀⣾⢁⣾⣧⡀⠱⡀⠹⣿⣧⡀⢠⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠑⠤⢄⣀⣀⡀⢹⠀⠀⠀⣼⣿⣿⣷⣾⣿⢱⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⣿⣿⣦⣽⣾⣿⣿⡗⠀⣷⠀⢹⡿⠁⠸⣿⣿⣿⣧⠀⠀⡠⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠒⠚⠛⠛⠛⠻⠿⠿⢸⣿⣿⣿⣿⣤⣤⣄⠀⠀⠀
⠀⣰⣾⣿⣿⣿⣿⣿⣿⣿⡎⢿⣿⠁⠀⢸⠀⢸⠁⠀⠀⠹⣿⠋⠸⠀⠐⢋⠇⣠⠀⣀⡄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢘⣿⣿⣿⣿⣿⣿⣷⠀⠀
⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢀⣁⣀⣀⣼⠀⢸⣤⣤⣤⣤⣤⣤⣤⠀⠀⠸⠊⠘⠊⠈⠉⠉⠉⠁⠀⠀⠉⡝⢷⣶⣶⣶⡶⠂⣤⣀⠀⡀⢀⣿⣿⣿⣿⣿⣿⣿⠁⠀
⠀⠘⠿⢿⠿⢿⣿⣿⣿⣿⣷⢻⡿⠻⣿⣿⠀⢸⣿⣿⡟⢻⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡐⠀⠈⢻⣿⡿⠁⠀⠹⣿⣿⣿⣿⣿⣿⡏⠻⠿⠛⠁⠀⠀
⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⢸⣇⢠⣿⡿⠀⢸⣿⣿⣄⣠⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣎⠀⠀⠀⢠⣿⡇⠀⠀⢀⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⡿⠞⠿⠟⠛⡇⠀⣾⣿⣿⣿⣿⡏⠀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣠⣿⣿⣿⣄⣀⣰⣿⣿⣿⡄⢀⣾⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⡖⠉⠉⠉⠉⢀⣀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⣿⡿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣤⣤⣀⡀⠀⠀
⠠⣴⣾⣿⣷⡀⠀⣠⡾⠻⣿⣷⣄⡀⠀⡏⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⢀⣤⢶⡦⢀⣴⠶⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⢠⣤⡤⠀⠀⠈⠛⠉⠙⠿⠛⠿⢿⣿⣿⣿⠇
⠀⠈⢻⣿⡏⠀⣰⣿⠃⠀⠈⣿⠟⠁⢰⠃⠀⣀⢀⠀⠀⢀⠄⠀⢀⡀⢸⣿⣤⠀⣸⣿⠴⢛⣧⠀⠀⡀⠀⣀⠀⠀⠀⢈⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁⠀
⠀⠀⢸⣿⡇⠀⣿⣿⠀⠀⠀⠀⠀⠀⢸⠀⢾⣿⠻⠗⠸⣿⣄⣼⠏⠐⢻⣿⠀⠐⣿⣿⠀⣿⡏⠀⣾⡟⢻⣿⠀⣾⡿⢻⣿⡇⣰⡶⢶⣄⢠⣶⣶⣶⡀⠀⣿⡟⠀⠀
⠀⠀⢸⣿⡇⠐⣿⡟⠀⠀⢀⣀⣀⡀⢸⠀⢸⣿⠀⠀⠀⢹⣿⠏⠀⠀⢸⣿⠀⠀⢻⣿⠀⣼⣿⠀⣿⡇⢸⣿⠀⣿⡇⢸⣿⡇⣿⡇⢸⣿⠀⣿⡇⠛⠁⠀⣿⡇⠀⠀
⠀⠀⢸⣿⡇⠀⣿⣧⠀⠈⢹⣿⣿⠁⠸⠀⠼⠿⠄⠀⣀⡼⠋⠀⢀⣀⣸⡿⠀⣀⣼⡏⠀⠛⠛⠠⠟⠓⠾⠿⠄⢿⡷⣾⣿⡇⢿⣇⣸⡿⢀⣿⡇⠀⠀⠀⣿⡇⠀⠀
⠀⠀⣸⣿⡇⠀⢿⣿⣇⠀⠀⣿⣿⡀⠀⠀⠀⠀⠙⠟⠋⠀⠀⠀⠀⠙⠛⠁⠀⠙⠛⠁⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠀⠉⠉⠙⠂⠀⠸⣿⡇⠀⠀
⠀⠀⣿⣿⡇⠀⠈⣿⣿⣦⣀⣿⡿⠷⠀⣦⣤⣴⣶⣶⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣶⣶⣶⣶⣶⣤⣤⣤⣤⣤⣄⠀⠀⠀⠀⠀⣿⡇⠀⠀
⠀⠀⣿⣿⡇⠀⠀⠘⠿⠛⠉⠀⠀⠀⠀⣿⣿⣿⣟⢿⠏⠉⠉⠉⢻⣿⣿⣁⣿⡏⠙⢤⡀⠀⠀⠀⠈⢫⡉⢉⣍⣉⣿⣿⣿⣿⡟⠿⠿⢿⣿⣿⣶⣶⣶⣤⣿⣇⠀⠀
⠀⠀⣿⠿⣇⣀⡀⠀⠀⠤⠔⠒⠒⠒⠺⣿⣿⣿⣿⣷⡄⠀⠀⠀⠈⠿⠿⠿⢿⡇⣠⣿⣿⣦⡀⠀⠀⠀⠈⠉⠻⣿⣿⣿⣿⠏⠀⠀⠀⠀⠉⠉⠙⠛⠛⠛⠿⠿⠀⠀
⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣦⣀⣀⠀⠀⠀⡄⣨⡇⠘⣿⣿⡿⢙⣦⣀⣀⣀⣢⣠⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣮⣙⠿⣿⡇⠀⠈⢟⣤⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⠋⠙⢿⣿⣿⣿⣷⣮⣅⣠⣴⣿⣿⣿⣿⠟⠉⠀⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
					''')
				break
			elif which_door == 'blue':
				print("Oh, snap! You lost! You are now in the realms of not knowing!")
			else:
				print("Please, try again:")
		elif go_or_stay == 'swim':
			print("Game over! You encountered a deadly Hydra!")
			break
		else:
			print("Please, try again:")
	elif direction == 'left':
		print("Game over! You have found a lioness protecting her cubs!")
		break
	else:
		print("Please, try again:")