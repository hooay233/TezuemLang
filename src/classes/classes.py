from copy import deepcopy
import sys
from codeRunner import *

class TezList(list):
	...

class Undef:
	def __str__(self) -> str:
		return "null"
	def __repr__(self) -> str:
		return "null"
null = Undef()

var = {
	"true": 1,
	"false": 0,
	"__IOflush__": sys.stdout
}

cfn = lambda: (funcs if thisCodeblock=="__main__" else thisCodeblock.fn)

thisCodeblock = "__main__"
class Codeblock:
	
	def __init__(self, codes: list) -> None:
		self.codes = codes
		self.lastCodeblock = thisCodeblock
	
	def do(self, **Functions):
		# print(self.lastCodeblock)
		global thisCodeblock, stopNow
		
		if self.lastCodeblock=="__main__":
			funcs = globals()["funcs"]
		else:
			funcs = self.lastCodeblock.fn
		thisCodeblock = self
		
		self.fn = deepcopy(funcs)
		rtnv = 0
		
		def tezCodesReturn(*args):
			global thisCodeblock, stopNow
			nonlocal self, rtnv
			
			arg = evalCodes(args, cfn())
			if len(arg)==0: rtnv = arg[0]
			thisCodeblock = self.lastCodeblock
			stopNow[0] = True
			self.codes = []
		
		self.fn["ret"] = tezCodesReturn
		# print(self.codes)
		
		# print(self.fn)
		self.fn.update(Functions)
		# print(self.fn)
		# print(self.fn["arg"])
		
		runCodes(self.codes, self.fn)
		return rtnv

class tezList(list):
	...

class tezFunc:
	def __init__(self, *args) -> None:
		cb = Codeblock(args[-1])
		def f(*arg):
			a = evalCodes(arg)
			a = tezList(a)
			tezarg = lambda *args: (a if len(args)==0 else a[args[0]])
			return cb.do(**{"arg":tezarg})
		funcs[args[0]] = f
