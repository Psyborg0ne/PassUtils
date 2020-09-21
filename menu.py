from generator import passGenerate
from tester import passCheck
from utils import clear, printc
import time

menu = {"G": "enerate", "T": "est", "E": "xit"}

def mainMenu(clean, colors):
	while True:
		clear(clean, colors)
		for i,j in menu.items():
			printc(f"{12 * ' '}{colors['green']}[{i}]{colors['none']}{j}")
		mainChoice = str(input("\n\n\n>>>")).lower()

		if mainChoice == 'g':
			passGenerate(clean, colors)
		elif mainChoice == 't':
			passCheck(clean, colors)
		elif mainChoice == 'e':
			clear(clean, colors)
			time.sleep(1)
			printc(f"{colors['green']}Thanks for using!")
			time.sleep(2)
			printc(f"Visit {colors['cyan']}www.codeblins.online{colors['green']} for more fun stuff!")
			time.sleep(2)
			printc(f"psyborg0ne, changing passwords since 1997")
			time.sleep(5)
			exit()
