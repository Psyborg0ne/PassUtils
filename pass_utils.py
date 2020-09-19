from utils import sysCheck, printc, clear
from generator import passGenerate
from tester import passCheck
import string

menu = {"G": "enerate", "T": "est", "E": "xit"}

clean, colors = sysCheck()
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
		exit()
