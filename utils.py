import shutil, platform, os, time
TERM_X, TERM_Y = shutil.get_terminal_size()
numLevels = {0: "", 1: "K", 2: "M",
 3: "B", 4: "T", 5: "Quad",
  6: "Quint", 7: "Sext", 8: "Sept",
   9: "Oct", 10: "Non", 11: "Dec"}

def sysCheck():
	if ((platform.system() == 'Windows' and platform.release() == '10' and platform.version() >= '10.0.14393') or platform.system() == "Linux"):
		if (platform.system() == 'Windows'):
			import ctypes
			kernel32 = ctypes.windll.kernel32
			kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
			clear = lambda: os.system('cls')

		elif(platform.system() == "Linux"):
			clean = lambda: os.system('clear')

		colors = {"red": "\033[1;31m",
		"green": "\033[0;32m",
		"yellow": "\033[0;33m",
		"blue": "\033[1;34m",
		"cyan": "\033[1;36m",
		"none": "\033[0;0m"}

	else:
		clean = lambda: os.system('cls')
		colors = {"red": "",
		"green": "",
		"yellow": "",
		"blue": "",
		"cyan": "",
		"none": ""}
	return clean, colors

def clear(clean, colors):
	clean()
	printLogo(colors)

# Returns numbers above 1.000 with a suffix ex. 1K, 3M etc.
def formatBigNumber(num: int)-> str:
	level = 0
	while num >= 1000:
		num /= 1000.0
		level += 1

	level = 11 if level > 11 else level
	hrNum = f'{str(num).split(".")[0]} {numLevels[level]}+'
	return hrNum

# Returns bool based on Y/n question
def ynChoice(question: str) -> bool:
	while True:
		choiceVar = input(f"{question}Y/n: ")
		if choiceVar == 'y' or choiceVar == 'n':
			if choiceVar == 'y':
				return True
			elif choiceVar == 'n':
				return False

def printc(text: str):
	print(text.center(TERM_X))

def printLogo(colors):
	print(colors['green'])
	with open("./logo.txt") as f:
		for i in f:
			printc(i)
	print(colors['none'])

def continueAction(clean, colors):
	while True:
		choice = str(input(f"{colors['blue']}Again? Y/n: {colors['none']}")).lower()
		if choice == 'y' or choice == 'n':
			if choice == 'n':
				from pass_utils import main
				main()
			clear(clean, colors)
			break
