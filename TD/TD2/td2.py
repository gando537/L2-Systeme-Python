import os,sys,errno
'''
N_wait = 10
for i in range(N_wait):
	pid = os.fork()
	if pid == 0 :			#Child
		sys.exit(100 + i)
try : 						#Parent waits for all of its children to terminate
	pid,status = os.waitpid(pid, 0)
	while True :
		if os.WIFEXITED(status):
			print("child {} terminate normally whith exit status = {}".\
				format(pid,os.WEXITSTATUS(status)))
		else :
			print("child {} terminate abnormally".format(pid))
		pid,status = os.waitpid(-1, 0)

except OSError as e :
	print("waitpid error : {}, {}".format(errno.errorcode[e.errno], os.strerror(e.errno)))
	if e.errno == errno.ECHILD :
		print("No more children left. Bye")
sys.exit(0)

'''
'''
print("Hello")
pid = os.fork()
print("Ici : {} ".format(pid))
if pid != 0:
	pid_wait,status = os.waitpid(pid, 0)
	
	if pid_wait > 0:
		if os.WIFEXITED(status) != 0:
			print("là : {}".format(os.WEXITSTATUS(status)))
	print("Bye")
	sys.exit(2)
sys.exit(0)

'''























