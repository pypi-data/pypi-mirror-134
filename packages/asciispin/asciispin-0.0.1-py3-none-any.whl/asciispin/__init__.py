import time, sys

def asciispin(length,ts):
	n = 0
	seq = ["|","/","-","\\"]
	print()
	for x in range(length):
		n = (n+1) % 4
		sys.stdout.write("\r"+seq[n])
		sys.stdout.flush()
		time.sleep(ts)
