from multiprocessing import Process, Event
import os

def run(event):
	os.system('python cNode.py')
	event.set()

cores = 4
processes = []

flip = Event()

for core in range(cores):
	processes.append(Process(target=run,args=(flip,)))
	processes[core].start()


while 1:
	flip.wait(60)
	flip.clear()
	for i,process in enumerate(processes):
		if not process.is_alive():
			processes[i] = 	Process(target=run,args=(flip,))
			processes[i].start()
		
