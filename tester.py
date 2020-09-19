from getpass import getpass
from utils import ynChoice, formatBigNumber, continueAction, clear
import math, string

def passCheck(clean, colors):
	clear(clean, colors)
	while True:

		diffChars = 0
		passLength = 0
		showPass = ""

		while True:
			userPass = str(getpass("Password to check (4-32):"))
			if 4 <= len(userPass) <= 32:
				break
			print("Enter a 4 to 32 characters passwopr")

		passLength = len(userPass)
		fullLine = f'+{44 * "-"}|'
		passString = f'Password:{colors["yellow"]} {userPass}{colors["none"]}' if ynChoice("Show password?") else f'| Password:{colors["yellow"]} {len(userPass) * "*"}{colors["none"]} |'
		clear(clean, colors)
		print(f"{fullLine}\n| {passString}\n{fullLine}")

		if(any(x.islower() for x in userPass)):
			diffChars += len(string.ascii_lowercase)
		if(any(x.isupper() for x in userPass)):
			diffChars += len(string.ascii_uppercase)
		if(any(x.isdigit() for x in userPass)):
			diffChars += len(string.digits)
		if(any(x in string.punctuation for x in userPass)):
			diffChars += len(string.punctuation)

		possiblePass = diffChars ** passLength
		passEntropy = math.log(possiblePass, 2)
		possiblePass = formatBigNumber(possiblePass)

		print(f"| Pool   :{colors['blue']} {diffChars} {colors['none']}")
		print(f"| Length :{colors['blue']} {passLength} {colors['none']}")
		print(f"| Entropy:{colors['blue']} {round(passEntropy, 1)} {colors['none']}")
		print(f"| Possile passwords :{colors['blue']} {possiblePass} {colors['none']}")

		if passEntropy < 29:
			strength = f"{colors['red']}Very Weak"
		elif 28 < passEntropy < 36:
			strength = f"{colors['red']}Weak"
		elif 35 < passEntropy < 60:
			strength = f"{colors['cyan']}Reasonable"
		elif 59 < passEntropy < 128:
			strength = f"{colors['green']}Stronk"
		elif passEntropy > 127:
			strength = f"{colors['green']}Very stronk"

		print(f"{fullLine}\nPassword Strength: {strength}{colors['none']}\n{fullLine}")

		continueAction(clean, colors)
