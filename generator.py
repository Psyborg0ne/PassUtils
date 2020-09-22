import string, random, pyperclip
from utils import ynChoice, continueAction, printc, clear

genSettings = {"LOWER": string.ascii_lowercase,
 "UPPER": string.ascii_uppercase,
  "NUMERIC": string.digits,
   "SPECIAL": string.punctuation}

def passGenerate(clean, colors):
	clear(clean, colors)
	while True:
		while True:
			while True:
				try:
					passLength = int(input("Password length (4-32): "))
					break
				except:
					print("Enter a number between 4 and 32")

			if 4 <= passLength <= 32:
				break
			print("Enter a number between 4 and 32")
		while True:
			availableLetters = ""
			charsAdded = {"Length": passLength}
			if ynChoice("Include 'lowercase'?"):
				availableLetters += genSettings['LOWER']
				charsAdded['Lower'] = f"{colors['blue']}Yes"
			else:
				charsAdded['Lower'] = f"{colors['red']}No"
			if ynChoice("Include 'UPPER'?"):
				availableLetters += genSettings['UPPER']
				charsAdded['Upper'] = f"{colors['blue']}Yes"
			else:
				charsAdded['Upper'] = f"{colors['red']}No"
			if ynChoice("Include '12345'?"):
				availableLetters += genSettings['NUMERIC']
				charsAdded['Numeric'] = f"{colors['blue']}Yes"
			else:
				charsAdded['Numeric'] = f"{colors['red']}No"
			if ynChoice("Include '!@#$%^'?"):
				availableLetters += genSettings['SPECIAL']
				charsAdded['Special'] = f"{colors['blue']}Yes"
			else:
				charsAdded['Special'] = f"{colors['red']}No"
			if availableLetters != "":
				break
			clear(clean, colors)

		passGen = ''.join((random.choice(availableLetters) for i in range(passLength)))
		fullLine = f'{colors["none"]}+{44 * "-"}|'
		clear(clean, colors)
		print(f"{fullLine}\n| Password: {colors['yellow']}{passGen}\n{fullLine}" )
		for i, j in charsAdded.items():
			print(f"{colors['none']}| {i}: {j}")
		print(fullLine)
		if ynChoice(f"{colors['yellow']}Copy password to clipboard?"):
			pyperclip.copy(passGen)
		continueAction(clean, colors)
