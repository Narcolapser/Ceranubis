###################################################################################################
#	Project:	Ceranubis
#	Programer:	Toben "Littlefoot" Archer
#	Date:		2012-07-24
#	Purpose:	cClient is the client library for the ceranubis system. its purpose is to 
#		Take batched jobs from the user and drop them into the system's database. where 
#		nodes will proceed to bring the data down for processing.
#################################################

import postgresql
import random

class Project:
	def __init__(self,serverIP,projectCode,targetFunction,listOfArgument):
		self.SIP = serverIP
		self.code = projectCode
		self.target = targetFunction
		self.args = listOfArgument
		try:
			db = postgresql.open("pq://ceranubis:raidersrow@" + self.SIP + "/ceranubis")
			self.connected = True
		except:
			self.connected = False
			return

		#insert the project into the database
		self.PID = random.randint(0,2147483647)
		db.execute("INSERT INTO projects VALUES("+str(self.PID)+",false,'"+self.code+"','"+self.target+"')")

		#insert the arguments into the database:
		for arg in self.args:
			AID = random.randint(0,2147483647)
			db.execute("INSERT INTO arguments VALUES("+str(AID)+","+str(self.PID)+",'"+arg+"')")

	def status(self):
		try:
			db = postgresql.open("pq://ceranubis:raidersrow@" + self.SIP + "/ceranubis")
			self.connected = True
		except:
			self.connected = False
			return False
		
		getNumDone = db.prepare("SELECT COUNT(result) AS done FROM arguments WHERE result IS NOT NULL  AND arguments.projid = $1;")
		getNumArg = db.prepare("SELECT COUNT(arg) AS overall FROM arguments WHERE arguments.projid = $1;")
		done = getNumDone(self.PID)
		arg = getNumArg(self.PID)
		return((done[0][0],arg[0][0]))
		


	def results(self):
		try:
			db = postgresql.open("pq://ceranubis:raidersrow@" + self.SIP + "/ceranubis")
			self.connected = True
		except:
			self.connected = False
			return False

		getRes = db.prepare("SELECT arg,result from arguments where result is not null;")	
		return getRes()

#def commitProject(serverIP,projectCode,targetFunction,listOfArgument):
#	p = Project(serverIP,projectCode,targetFunction,listOfArgument)
#	if p.connected:
#		return p
#	return False

#q = commitProject('localHost','derpaderpyderp','monkies!',['wooooooo','arg2!'])
#if q:
#	print("WOOOOOOOOOOOOOOOOO")
#input()
#stat = q.status()
#print(stat)

#res = q.results()
#print(res)

#.S.D.G.#
