from utils import sysCheck
from menu import mainMenu

def main():
	clean, colors = sysCheck()
	mainMenu(clean, colors)

main()
