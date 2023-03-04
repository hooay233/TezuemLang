from lib import *

def test(*args):
	arg = evalCodes(args, cfn())
	if len(arg)==0:
		print("this is test lib")
	else:
		def tezu(*args):
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
			print  ("\033[0;31;40m  ######\033[0m")
			print("\ngithub: https://github.com/hooay233/TezuemLang")
		def homo(*args):
			return 114514
		f = {
			"tezu": tezu,
			"homo": homo,
			"pi": (lambda *args: 3.1415926535)
		}
		return f[arg[0]]()

funcs.update({
	"test": test,
	"TEZU": (lambda *args: (print  ("\033[0;31;40m  ######\033[0m", end=""),print  ("\033[0;33;40m  ######\033[0m", end=""),print  ("\033[0;32;40m  ######\033[0m", end=""),print("\n\033[0;31;40m  ##    \033[0m", end=""),print  ("\033[0;33;40m    ##  \033[0m", end=""),print  ("\033[0;32;40m  ##    \033[0m", end=""),print("\n\033[0;31;40m  ##    \033[0m", end=""),print  ("\033[0;33;40m    ##  \033[0m", end=""),print  ("\033[0;32;40m  ######\033[0m", end=""),print("\n\033[0;31;40m  ##    \033[0m", end=""),print  ("\033[0;33;40m    ##  \033[0m", end=""),print  ("\033[0;32;40m  ##    \033[0m", end=""),print("\n\033[0;31;40m  ######\033[0m", end=""),print  ("\033[0;33;40m    ##  \033[0m", end=""),print  ("\033[0;32;40m  ######\033[0m", end=""),print("\n"),print  ("\033[0;36;40m  ######\033[0m", end=""),print  ("\033[0;34;40m  ##  ##\033[0m", end=""),print  ("\033[0;31;40m  ######\033[0m", end=""),print("\n\033[0;36;40m      ##\033[0m", end=""),print  ("\033[0;34;40m  ##  ##\033[0m", end=""),print  ("\033[0;31;40m      ##\033[0m", end=""),print("\n\033[0;36;40m  ##    \033[0m", end=""),print  ("\033[0;34;40m  ##  ##\033[0m", end=""),print  ("\033[0;31;40m      ##\033[0m", end=""),print("\n\033[0;36;40m  ##    \033[0m", end=""),print  ("\033[0;34;40m  ##  ##\033[0m", end=""),print  ("\033[0;31;40m      ##\033[0m", end=""),print("\n\033[0;36;40m  ######\033[0m", end=""),print  ("\033[0;34;40m  ######\033[0m", end=""),print  ("\033[0;31;40m  ######\033[0m"),print("\ngithub: https://github.com/hooay233/TezuemLang"))),
	
})

