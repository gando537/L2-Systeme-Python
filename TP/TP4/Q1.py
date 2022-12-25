import os,sys

pid = os.fork()
if pid == 0:
	for i in range(5):
		os.write(1,b'a')
	sys.exit(0)
for i in range(5):
		os.write(1,b'b')
sys.exit(0)