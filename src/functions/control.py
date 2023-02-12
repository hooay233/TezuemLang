
from codeRunner import *
from classes.classes import *




def tezCodes(*args):
	return Codeblock(list(args[0]))

def tezAdd(*args):
	arg = evalCodes(args, cfn())
	n = arg[0]
	for i in arg[1:]:
		n += i
	return n

def tezSub(*args):
	arg = evalCodes(args, cfn())
	if len(arg)==1:
		return -(arg[0])
	n = arg[0]
	for i in arg[1:]:
		n -= i
	return n

def tezMult(*args):
	arg = evalCodes(args, cfn())
	n = arg[0]
	for i in arg[1:]:
		n *= i
	return n

def tezDivi(*args):
	arg = evalCodes(args, cfn())
	n = arg[0]
	for i in arg[1:]:
		n /= i
	return n

def tezEq(*args):
	arg = evalCodes(args, cfn())
	b = ""
	for i in arg:
		b += repr(i)
		b += "=="
	b = b[:-2]
	# print(b)
	return eval(b)

def tezGt(*args):
	arg = evalCodes(args, cfn())
	b = ""
	for i in arg:
		b += repr(i)
		b += ">"
	b = b[:-1]
	return eval(b)

def tezLt(*args):
	arg = evalCodes(args, cfn())
	b = ""
	for i in arg:
		b += repr(i)
		b += "<"
	b = b[:-1]
	return eval(b)

def tezRem(*args):
	arg = evalCodes(args, cfn())
	n = arg[0]
	for i in arg[1:]:
		n %= i
	return n

def tezDiviSub(*args):
	arg = evalCodes(args, cfn())
	n = arg[0]
	for i in arg[1:]:
		n = n//i
	return n

def tezDiviAdd(*args):
	arg = evalCodes(args, cfn())
	n = arg[0]
	for i in arg[1:]:
		if n%i!=0:
			n = n//i+1
		else:
			n = n//i
	return n


def tezDo(*args):
	arg = evalCodes(args, cfn())
	if type(arg[0])==Codeblock:
		return arg[0].do()

def tezForever(*args):
	arg = evalCodes(args, cfn())
	noBreak = True
	if len(arg)==1 and type(arg[0])==Codeblock:
		def tezBreak(*args):
			nonlocal noBreak, arg
			noBreak = False
			# print(arg[0].codes)
			arg[0].codes = []
			# print(arg[0].codes)
			stopNow[0] = True
		while noBreak:
			arg[0].do(**{"break": tezBreak})

def tezIf(*args):
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
		# print(b, repr(var["n"]))

funcs.update({
	"exit": exit,
	"quit": quit,
	"+": tezAdd,
	"-": tezSub,
	"*": tezMult,
	"/": tezDivi,
	"=": tezEq,
	">": tezGt,
	"<": tezLt,
	"%": tezRem,
	"/-": tezDiviSub,
	"/+": tezDiviAdd,
	"codes": tezCodes,
	"do": tezDo,
	"fn": tezFunc,
	"forever": tezForever,
	"if": tezIf,
})
