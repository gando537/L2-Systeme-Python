import os, sys, time , signal, errno


def prog_td2():
	nb_children = 5

	for i in range(nb_children):
		pid = os.fork()
		if pid == 0 :
			print("pid_fils = {}".format(os.getpid()))
			time.sleep(20)
			sys.exit(100 + i)
	try : 						#Parent waits for all of its children to terminate
		pid,status = os.waitpid(pid, 0)
		while True :
			if os.WIFEXITED(status):
				print("child {} terminate normally whith exit status = {}".\
					format(pid,os.WEXITSTATUS(status)))
			else :
				print("child {} terminate abnormally, signal = {}".format(pid, os.WTERMSIG(status)))
			pid,status = os.waitpid(-1, 0)

	except OSError as e :
		print("waitpid error : {}, {}".format(errno.errorcode[e.errno], os.strerror(e.errno)), file=sys.stderr)
		if e.errno == errno.ECHILD :
			print("No more children left. Bye")
	sys.exit(0)

prog_td2()



















