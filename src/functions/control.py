from sys import exit

from codeRunner import *
from classes.classes import *




def tezuCodes(*args):
	return Codeblock(list(args[0]))

def tezuAdd(*args):
	arg = evalCodes(args, cfn())
	n = arg[0]
	for i in arg[1:]:
		n += i
	return n

def tezuSub(*args):
	arg = evalCodes(args, cfn())
	if len(arg)==1:
		return -(arg[0])
	n = arg[0]
	for i in arg[1:]:
		n -= i
	return n

def tezuMult(*args):
	arg = evalCodes(args, cfn())
	n = arg[0]
	for i in arg[1:]:
		n *= i
	return n

def tezuDivi(*args):
	arg = evalCodes(args, cfn())
	n = arg[0]
	for i in arg[1:]:
		n /= i
	return n

def tezuEq(*args):
	arg = evalCodes(args, cfn())
	b = ""
	for i in arg:
		b += repr(i)
		b += "=="
	b = b[:-2]
	# print(b)
	return eval(b)

def tezuGt(*args):
	arg = evalCodes(args, cfn())
	b = ""
	for i in arg:
		b += repr(i)
		b += ">"
	b = b[:-1]
	return eval(b)

def tezuLt(*args):
	arg = evalCodes(args, cfn())
	b = ""
	for i in arg:
		b += repr(i)
		b += "<"
	b = b[:-1]
	return eval(b)

def tezuRem(*args):
	arg = evalCodes(args, cfn())
	n = arg[0]
	for i in arg[1:]:
		n %= i
	return n

def tezuDiviSub(*args):
	arg = evalCodes(args, cfn())
	n = arg[0]
	for i in arg[1:]:
		n = n//i
	return n

def tezuDiviAdd(*args):
	arg = evalCodes(args, cfn())
	n = arg[0]
	for i in arg[1:]:
		if n%i!=0:
			n = n//i+1
		else:
			n = n//i
	return n


def tezuDo(*args):
	arg = evalCodes(args, cfn())
	if type(arg[0])==Codeblock:
		return arg[0].do()

def tezuForever(*args):
	arg = evalCodes(args, cfn())
	noBreak = True
	if len(arg)==1 and type(arg[0])==Codeblock:
		def tezuBreak(*args):
			nonlocal noBreak, arg
			noBreak = False
			arg[0].codes = []
			stopNow[0] = True
		while noBreak:
			arg[0].do(**{"break": tezuBreak})

def tezuIf(*args):
	arg = evalCodes(args, cfn())
	for i in range(len(arg)):
		if i==0:
			b = arg[i]
		elif i==1 and b:
			return arg[i].do()
		elif arg[i]=="elif":
			i += 1
			b = arg[i]
			i += 1
			if b:
				return arg[i].do()
		elif arg[i]=="else":
			i += 1
			return arg[i].do()

funcs.update({
	"exit": exit,
	"quit": exit,
	"+": tezuAdd,
	"-": tezuSub,
	"*": tezuMult,
	"/": tezuDivi,
	"=": tezuEq,
	">": tezuGt,
	"<": tezuLt,
	"%": tezuRem,
	"/-": tezuDiviSub,
	"/+": tezuDiviAdd,
	"codes": tezuCodes,
	"do": tezuDo,
	"fn": tezuFunc,
	"forever": tezuForever,
	"if": tezuIf,
})
