import sys

from functions.control import *
from functions.filesio import *


def main():
	if len(sys.argv)==1:
		while True:
			runCodes(getTezCodeListOfPy(input("\n>>> ")))
	else:
		with open(sys.argv[1]) as f:
			c = f.read()
		runCodes(getTezCodeListOfPy(c))

if __name__=="__main__":
	main()