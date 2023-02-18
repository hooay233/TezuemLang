import re

funcs = {}

test = 0

def getTezuCodeListOfPy(s: str):
	global test
	n = 0
	l = "["
	isstr = False
	char = 0
	line = 1
	nextTerm = False
	code = re.sub("/\\..*?(\\./|$)", "", re.sub("//.*?(\n|$)", "", s))
	
	lineContinua = False
	isastring = False
	escape = 0
	for i in code:
		char += 1
		if i=="[" and not isastring:
			if isstr:
				isstr = False
				l += '"'
				nextTerm = True
			
			n += 1
			l += "["
			nextTerm = False
		elif i=="]" and not isastring:
			if isstr:
				isstr = False
				l += '"'
				nextTerm = True
			
			n -= 1
			l += "]"
			nextTerm = True
		elif (i==" " or i=="\n" or i=="\r" or i=="\t") and (not (isastring)) and (not lineContinua):
			if nextTerm and not isstr:
				l += ",\n"
				nextTerm = False
			
			if isstr:
				isstr = False
				l += '",\n'
				nextTerm = True
				
		elif (i.isdigit() or i==".") and not isastring:
			if isstr:
				isstr = False
				l += '"'
				nextTerm = True
			
			l += i
			nextTerm = True
		elif i=='"':
			if isstr:
				isstr = False
				l += '"'
				nextTerm = True
			
			if isastring and (not escape):
				isastring = False
				l += '"'
				nextTerm = True
			else:
				isastring = True
				nextTerm = False
		elif i=="\\":
			if isstr:
				isstr = False
				l += '"'
				nextTerm = True
			
			if isastring:
				escape = 1
			else:
				lineContinua = True
		elif not isastring:
			if isstr:
				l += i
			else:
				l += '"'+i
				isstr = True
		if isastring:
			if not escape and i!="\\":
				l += i
			elif escape==2:
				l += "\\"+i
				escape = 0
			elif escape==1:
				escape = 2
		if i=="\n":
			line += 1
			char = 1
	
	l += "]"
	# print(l)
	return eval(l)

def evalCodes(args: tuple, funcs: dict=funcs):
	argsList = list(args)
	for i in range(len(argsList)):
		if type(argsList[i])==list:
			argsList[i] = runaFunc(argsList[i][0], argsList[i][1:], funcs)
	return tuple(argsList)

def runaFunc(name: str, args: list, funcs: dict=funcs):
	if type(name)==str:
		if len(args)==0:
			return funcs[name]()
		else:
			return funcs[name](*args)
	elif type(name)==list:
		return runaFunc("codes", [[name]+args, funcs])

stopNow = [False]
def runCodes(code: list, funcs: dict=funcs):
	global stopNow
	for i in code:
		# print(globals()["stopNow"])
		if stopNow[0]:
			stopNow[0] = False
			return
		runaFunc(i[0], i[1:], funcs)
