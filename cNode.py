###################################################################################################
#	Project:	Ceranubis
#	Programer:	Toben "Littlefoot" Archer
#	Date:		2012-07-18
#	Purpose:	cNode is the programing behind running the requested code remotely.
#################################################

import random
import imp
import sys
import os

class Project:
	def __init__(self,ID,code,target):
		self.PID = ID
		self.code = code
		self.target = target

	def doWork(self):
		arg,AID = self.getArg()
		if arg:
			result = run(self.target,arg,self.code)
			self.returnResult(AID,result)
			return True
		else:
			return False
		

	def getArg(self):
		return random.choice([(1,0),(2,1),(3,2),(4,3),(None,None)])

	def returnResult(self,AID,result):
		f = open('outs','a')
		f.write("AID: " + str(AID) + " result: " + str(result) + "\n")
		f.close()
#		print "PID: " + str(os.getpid()) + " AID: " + str(AID) + " result: " + str(result)
		

def getProject():
	return random.choice([Project(0,"import math\n\ndef sqrt(val):\n\treturn math.sqrt(val)","sqrt"),
			Project(0,"import math\n\ndef log(val):\n\treturn math.log10(val)","log")])

def run(target,arg,code):
	exec("ret = " + target + "(arg)")
	return ret

p = getProject()
exec(p.code)
while p.doWork():
	pass

#.S.D.G.#
