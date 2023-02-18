import sys

from functions.control import *
from functions.filesio import *

def printTezuLogo():
	print  ("\033[0;31;40m  ######\033[0m", end="")
	print  ("\033[0;33;40m  ######\033[0m", end="")
	print  ("\033[0;32;40m  ######\033[0m", end="")
	print("\n\033[0;31;40m  ##    \033[0m", end="")
	print  ("\033[0;33;40m    ##  \033[0m", end="")
	print  ("\033[0;32;40m  ##    \033[0m", end="")
	print("\n\033[0;31;40m  ##    \033[0m", end="")
	print  ("\033[0;33;40m    ##  \033[0m", end="")
	print  ("\033[0;32;40m  ######\033[0m", end="")
	print("\n\033[0;31;40m  ##    \033[0m", end="")
	print  ("\033[0;33;40m    ##  \033[0m", end="")
	print  ("\033[0;32;40m  ##    \033[0m", end="")
	print("\n\033[0;31;40m  ######\033[0m", end="")
	print  ("\033[0;33;40m    ##  \033[0m", end="")
	print  ("\033[0;32;40m  ######\033[0m", end="")
	
	print("\n")
	
	print  ("\033[0;36;40m  ######\033[0m", end="")
	print  ("\033[0;34;40m  ##  ##\033[0m", end="")
	print  ("\033[0;31;40m  ######\033[0m", end="")
	print("\n\033[0;36;40m      ##\033[0m", end="")
	print  ("\033[0;34;40m  ##  ##\033[0m", end="")
	print  ("\033[0;31;40m      ##\033[0m", end="")
	print("\n\033[0;36;40m  ##    \033[0m", end="")
	print  ("\033[0;34;40m  ##  ##\033[0m", end="")
	print  ("\033[0;31;40m      ##\033[0m", end="")
	print("\n\033[0;36;40m  ##    \033[0m", end="")
	print  ("\033[0;34;40m  ##  ##\033[0m", end="")
	print  ("\033[0;31;40m      ##\033[0m", end="")
	print("\n\033[0;36;40m  ######\033[0m", end="")
	print  ("\033[0;34;40m  ######\033[0m", end="")
	print  ("\033[0;31;40m  ######\033[0m", end="")
	print("\ngithub: ...")

def main():
	if len(sys.argv)==1:
		printTezuLogo()
		while True:
			runCodes(getTezuCodeListOfPy(input("\n>>> ")))
	else:
		with open(sys.argv[1]) as f:
			c = f.read()
		runCodes(getTezuCodeListOfPy(c))

if __name__=="__main__":
	main()