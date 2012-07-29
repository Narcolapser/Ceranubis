import cClient
import time

f = open("runcode.py",'r')
code = f.read()
target = 'run'
argsNums = []
for i in range(100):
	argsNums.append(i+1)
args = []
for i in argsNums:
	args.append(str(i))


p = cClient.commitProject('localHost',code,target,args)

s = p.status()

while s[0] != s[1]:
	time.sleep(5)
	s = p.status()
	print(s)

r = p.results()

print(r)
