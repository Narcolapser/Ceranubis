###################################################################################################
#	Project:	Ceranubis
#	Programer:	Toben "Littlefoot" Archer
#	Date:		2012-07-18
#	Purpose:	cNode is the programing behind running the requested code remotely.
#################################################

import random
import imp
import sys

class Project:
	def __init__(self,ID,code,target):
		self.PID = ID
		self.code = code
		self.target = target
		importCode(code,"project",1)

	def doWork(self):
		arg,AID = self.getArg()
		result = run(self.target,arg,self.code)
		self.returnResult(AID,result)

	def getArg(self):
		return random.choice([(1,0),(2,1),(3,2),(4,3)])

	def returnResult(self,AID,result):
		print "AID: " + str(AID) + " result: " + str(result)
		

def getProject():
	return Project(0,"import math\n\ndef sqrt(val):\n\treturn math.sqrt(val)","sqrt")

def importCode(code,name,add_to_sys_modules=0):
	"""
	Import dynamically generated code as a module. code is the
	object containing the code (a string, a file handle or an
	actual compiled code object, same types as accepted by an
	exec statement). The name is the name to give to the module,
	and the final argument says wheter to add it to sys.modules
	or not. If it is added, a subsequent import statement using
	name will return this module. If it is not added to sys.modules
	import will try to load it in the normal fashion.

	import foo
	
	is equivalent to
	
	foofile = open("/path/to/foo.py")
	foo = importCode(foofile,"foo",1)

	Returns a newly generated module.
	"""
	module = imp.new_module(name)

	exec code in module.__dict__
	if add_to_sys_modules:
		sys.modules[name] = module

	return module


def run(target,arg,code):
	exec(code)
	print dir()
	exec("ret = " + target + "(arg)")
	return ret

p = getProject()
p.doWork()
p.doWork()
p.doWork()

#.S.D.G.#
