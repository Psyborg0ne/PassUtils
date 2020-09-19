import math, getpass, platform, os, time, shutil
import string, random

TERM_X = shutil.get_terminal_size().columns

numLevels = {0: "", 1: "K", 2: "M", 3: "B", 4: "T", 5: "Quad", 6: "Quint", 7: "Sext", 8: "Sept", 9: "Oct", 10: "Non", 11: "Dec", 12: 'Unde', 13: "Duode", 14: "Trede", 15: "Quattuorde"}

def userChoice(choiceVar, question: str):

	while True:
		choiceVar = input(f"{question}Y/n: ")
		if choiceVar == 'y' or choiceVar == 'n':
			if choiceVar == 'y':
				return True
			elif choiceVar == 'n':
				return False

def formatBigNumber(num: int):
	level = 0
	while num >= 1000:
		num /= 1000.0
		level += 1
	hrNum = f'{str(num).split(".")[0]}{numLevels[level]}'
	return hrNum

def printLogo():
	logo = f"|{colors['cyan']} psyborg0ne's password utils{colors['none']} |"
	print(f"+{(len(logo) - 15) * '-'}+\n{logo}\n+{(len(logo) - 15) * '-'}+")

def printc(text: str, end=""):
	print(text.center(TERM_X), end)

if ((platform.system() == 'Windows' and platform.release() == '10' and platform.version() >= '10.0.14393') or platform.system() == "Linux"):
	if (platform.system() == 'Windows'):
		import ctypes
		kernel32 = ctypes.windll.kernel32
		kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
		clear = lambda: os.system('cls')

	elif(platform.system() == "Linux"):
		clear = lambda: os.system('clear')

	colors = {"red": "\033[1;31m",
	"green": "\033[0;32m",
	"yellow": "\033[0;33m",
	"blue": "\033[1;34m",
	"cyan": "\033[1;36m",
	"none": "\033[0;0m"}

else:
	clear = lambda: os.system('cls')
	colors = {"red": "",
	"green": "",
	"yellow": "",
	"blue": "",
	"cyan": "",
	"none": ""}

letterPool = {"lower": 26, "upper": 26, "numeric": 10, "special": 32}
genSettings = {"LOWER": string.ascii_lowercase, "UPPER": string.ascii_uppercase, "NUMERIC": string.digits, "SPECIAL": string.punctuation}
running = True

# while running:
# 	while True:
# 		printLogo()
# 		passLength = int(input("Password length (4-32): "))
# 		if 4 <= passLength <= 32:
# 			break
# 		clear()
# 	while True:
# 		availableLetters = ""
# 		letterChoice = ""
# 		if userChoice(letterChoice, "Include 'lowercase'?"):
# 			availableLetters += genSettings['LOWER']
# 		if userChoice(letterChoice, "Include 'UPPER'?"):
# 			availableLetters += genSettings['UPPER']
# 		if userChoice(letterChoice, "Include '12345'?"):
# 			availableLetters += genSettings['NUMERIC']
# 		if userChoice(letterChoice, "Include '!@#$%^'?"):
# 			availableLetters += genSettings['SPECIAL']
# 		if availableLetters != "":
# 			print(len(availableLetters))
# 			print(availableLetters)
# 			break
# 	passGen = ''.join((random.choice(availableLetters) for i in range(passLength)))
# 	print("Password: " + passGen)
# 	break

while running:
	R = 0
	L = 0
	showPass = ""

	while True:
		printLogo()
		userPass = str(getpass.getpass("Password to check (4-32):"))
		if 4 <= len(userPass) <= 32:
			break
		clear()
	while True:
		showPass = str(input("Show password?Y/n: ")).lower()
		if (showPass == 'y' or showPass == "n"):
			break
	clear()
	print(f"{colors['none']}+{(len(userPass) + 12) * '-'}+")
	print(f'| Password:{colors["yellow"]} {userPass}{colors["none"]} |') if showPass == "y" else print(f'| Password:{colors["yellow"]} {len(userPass) * "*"}{colors["none"]} |')

	if(any(x.islower() for x in userPass)):
		R += letterPool['lower']

	if(any(x.isupper() for x in userPass)):
		R += letterPool['upper']

	if(any(x.isdigit() for x in userPass)):
		R += letterPool['numeric']

	# TODO Add special character check
	L = len(userPass)
	possiblePass = R ** L
	E = math.log(possiblePass, 2)
	possiblePass = formatBigNumber(possiblePass)
	print(f"{colors['none']}+{(len(userPass) + 12) * '-'}+")
	print(f"| Password entered length    :{colors['blue']} {L} {colors['none']}")
	print(f"| No. of characters in pool  :{colors['blue']} {R} {colors['none']}")
	print(f"| No. of possible passwords  :{colors['blue']} {possiblePass} {colors['none']}")
	print(f"| Entropy for this password  :{colors['blue']} {round(E, 1)} {colors['none']}")
	print(f"{colors['none']}+{(len(userPass) + 13) * '-'}")
	print("Password Strength: ", end="")

	if E < 29:
		print(f"{colors['red']}Very Weak")
	elif 28 < E < 36:
		print(f"{colors['red']}Weak")
	elif 35 < E < 60:
		print(f"{colors['cyan']}Reasonable")
	elif 59 < E < 128:
		print(f"{colors['green']}Stronk")
	elif E > 127:
		print(f"{colors['green']}Very stronk")

	while True:
		choice = str(input(f"{colors['none']}Keep checking? Y/n: ")).lower()
		if choice == 'y' or choice == 'n':
			if choice == 'n':
				print(f"\n\n\n{colors['green']}Thanks for using!")
				time.sleep(1)
				print(f"Visit {colors['cyan']}www.codeblins.online{colors['green']} for more fun stuff!")
				time.sleep(2)
				print(f"psyborg0ne, changing passwords since 1997")
				time.sleep(1)
				running = False
			break
	clear()
