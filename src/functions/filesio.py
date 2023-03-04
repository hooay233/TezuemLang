import os

from codeRunner import *
from classes.classes import *

def tezuPut(*args):
	arg = evalCodes(args, cfn())
	print(*arg, end="" , file=var["__IOflush__"], flush=True)

def tezuAsk(*args):
	arg = evalCodes(args, cfn())
	print(*arg, end="")
	return input()

def tezuSet(*args):
	arg = evalCodes(args, cfn())
	if arg[1]=="to":
		var[arg[0]] = arg[2]
		return var[arg[0]]

def tezuGet(*args):
	arg = evalCodes(args, cfn())
	if len(arg)==1:
		return var[arg[0]]
	else:
		v = arg[0]
		for i in arg:
			v = v[i]
		return v

def tezuOpenFile(*args):
	arg = evalCodes(args, cfn())
	return open(*arg)

def tezuCloseFile(*args):
	arg = evalCodes(args, cfn())
	return arg[0].close()

def tezuReadFile(*args):
	arg = evalCodes(args, cfn())
	return arg[0].read()

def tezuWriteFile(*args):
	arg = evalCodes(args, cfn())
	return arg[0].write(*arg[1:])

def tezuFile(*args):
	arg = evalCodes(args, cfn())
	return {
		"open": tezuOpenFile,
		"read": tezuReadFile,
		"Write": tezuWriteFile,
		"close": tezuCloseFile,
	}[arg[0]](*arg[1:])

def tezuInclude(*args):
	arg = evalCodes(args, cfn())
	if arg[0][0]=="<" and arg[0][-1]==">":
		with open(os.getenv("APPDATA")+"\\Tezuem\\path") as f:
			p = f.read()
		with open(p+f"\\libs\\{arg[0][1:-1]}_init.py") as f:
			f.readline()
			c = f.read()
		exec(c, globals())
	else:
		with open(arg[0]) as f:
			runCodes(getTezuCodeListOfPy(f.read()))

def tezuChan(*args):
	arg = evalCodes(args, cfn())
	if type(arg[0])==str:
		var[arg[0]] = runaFunc(arg[1], (var[arg[0]],)+args[2:])

funcs.update({
	"put": tezuPut,
	"ask": tezuAsk,
	"set": tezuSet,
	"$": tezuGet,
	"chan": tezuChan,
	"file": tezuFile,
	"include": tezuInclude,
})