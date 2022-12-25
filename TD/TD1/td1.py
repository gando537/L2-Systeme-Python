import os, sys, time

parametre = int(sys.argv[1])
print(os.getpid())
for i in range(parametre):
	fils = os.fork()
	if fils == 0:
		print("fils %d = %d" % (i + 1, os.getpid()))
		sys.exit(0)