from codeRunner import *
from classes.classes import *

def tezPut(*args):
	arg = evalCodes(args, cfn())
	print(*arg, end="" , file=var["__IOflush__"], flush=True)

def tezAsk(*args):
	arg = evalCodes(args, cfn())
	print(*arg, end="")
	return input()

def tezSet(*args):
	# print("[[[",args, cfn)
	arg = evalCodes(args, cfn())
	if arg[1]=="to":
		var[arg[0]] = arg[2]
		return var[arg[0]]

def tezGet(*args):
	arg = evalCodes(args, cfn())
	if len(arg)==1:
		return var[arg[0]]
	else:
		v = arg[0]
		for i in arg:
			v = v[i]
		return v

def tezOpenFile(*args):
	arg = evalCodes(args, cfn())
	return open(*arg)

def tezCloseFile(*args):
	arg = evalCodes(args, cfn())
	return arg[0].close()

def tezReadFile(*args):
	arg = evalCodes(args, cfn())
	return arg[0].read()

def tezWriteFile(*args):
	arg = evalCodes(args, cfn())
	return arg[0].write(*arg[1:])

def tezFile(*args):
	arg = evalCodes(args, cfn())
	return {
		"open": tezOpenFile,
		"read": tezReadFile,
		"Write": tezWriteFile,
		"close": tezCloseFile,
	}[arg[0]](*arg[1:])

def tezInclude(*args):
	arg = evalCodes(args, cfn())
	if arg[0][1]=="<" and arg[0][-1]==">":
		...
	else:
		with open(arg[0]) as f:
			runCodes(getTezCodeListOfPy(f.read()))

def tezChan(*args):
	arg = evalCodes(args, cfn())
	if type(arg[0])==str:
		var[arg[0]] = runaFunc(arg[1], (var[arg[0]],)+args[2:])

funcs.update({
	"put": tezPut,
	"ask": tezAsk,
	"set": tezSet,
	"$": tezGet,
	"chan": tezChan,
	"file": tezFile,
	"include": tezInclude,
})