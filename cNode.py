###################################################################################################
#	Project:	Ceranubis
#	Programer:	Toben "Littlefoot" Archer
#	Date:		2013-02-18
#	Purpose:	cNode is the programing behind running the requested code remotely.
#################################################

import random
import imp
import sys
import os
import postgresql

class Project:
	def __init__(self,ID,code,target,SIP):
		self.PID = ID
		self.code = code
		self.target = target
		self.SIP = SIP
		self.db = postgresql.open("pq://ceranubis:raidersrow@" + self.SIP + "/ceranubis")
		self.update = self.db.prepare("Update arguments SET Result = $1 WHERE ArgID = $2 AND ProjID = $3;")
		self.arg = self.db.prepare("SELECT * FROM arguments WHERE result IS NULL")

	def doWork(self):
		AID,arg = self.getArg()
		if arg:
			result = doTheCodeThatWasSentByTheUserForCeranubisToProcessByAFunctionNamedSomethingTheUserWillNeverUseEVER(self.target,arg,self.code)
			self.returnResult(AID,result)
			return True
		else:
			return False
		

	def getArg(self):
		args = self.arg()
		try:
			arg = random.choice(args)
			return ((arg[0],arg[2]))
		except:
			return ((False,False))

	def returnResult(self,AID,result):
		self.update(result,AID,self.PID)
		
		

def getProject(SIP):
	db = postgresql.open("pq://ceranubis:raidersrow@" + SIP + "/ceranubis")
	getProj = db.prepare("SELECT * FROM projects WHERE NOT completed")
	proj = getProj()[0]
	return Project(proj[0],proj[2],proj[3],SIP)
	

def doTheCodeThatWasSentByTheUserForCeranubisToProcessByAFunctionNamedSomethingTheUserWillNeverUseEVER(target,arg,code):
	fetch = {'arg':arg,'target':target}
	exec(code,fetch,fetch)
	exec("ret = " + target + "(arg)",fetch,fetch)
	ret = fetch['ret']
	return ret

p = getProject('localhost')
exec(p.code) in globals()
while p.doWork():
	pass

#.S.D.G.#
