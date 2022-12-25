import os, sys, time , signal, errno

def chld_handler(sig, ignore):

	pid, status = os.waitpid(-1, 0)
	if os.WIFEXITED(status):
		print("***père*** chld {} termined normally with exit status = {}".format(pid,os.WEXITSTATUS(status)))

	else:
		print("***père*** child {} termined abnormally".format(pid))

if __name__ == "__main__":
	signal.signal(signal.SIGCHLD, chld_handler)

	for i in range(10):
		pid = os.fork()

		if pid == 0:
			print("---> fils (pid = {}). Je me termine.".format(os.getpid()))
			sys.exit(1 + i)
		print("***père*** fils crée, pid = {}".format(pid))

	while not 'saisie' in globals():
		try:
			saisie = input("**père** tapez quelque chose... ")
		except:
			pass
	print("**père** Terminé !")
	sys.exit(0)