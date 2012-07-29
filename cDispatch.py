from multiprocessing import Process, Event
import os
import time

def run(event):
	os.system('python3 cNode.py')
	event.set()

responseTime = 60
cores = 8
processes = []

flip = Event()

for core in range(cores):
	processes.append(Process(target=run,args=(flip,)))
	processes[core].start()


while 1:
	time.sleep(60)
	flip.wait(60)
	flip.clear()
	for i,process in enumerate(processes):
		if not process.is_alive():
			processes[i] = 	Process(target=run,args=(flip,))
			processes[i].start()
		
