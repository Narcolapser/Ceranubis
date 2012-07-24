###################################################################################################
#	Project:	Ceranubis
#	Programer:	Toben "Littlefoot" Archer
#	Date:		2012-07-24
#	Purpose:	cClient is the client library for the ceranubis system. its purpose is to 
#		Take batched jobs from the user and drop them into the system's database. where 
#		nodes will proceed to bring the data down for processing.
#################################################

class Project:
	def __init__(self,serverIP,projectCode,targetFunction,listOfArgument):
		self.SIP = serverIP
		self.code = projectCode
		self.target = targetFunction
		self.args = listOfArguments

	def status(self):
		pass

	def results(self):
		pass

def commitProject(serverIP,projectCode,targetFunction,listOfArgument):
	return Project(serverIP,projectCode,targetFunction,listOfArgument)

#.S.D.G.#t
