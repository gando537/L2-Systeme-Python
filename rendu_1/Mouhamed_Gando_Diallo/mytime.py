import time, signal, sys, os

if __name__ == '__main__':

	temp_debut = time.time()
	pid = os.fork()
	if pid == 0:
		if sys.argv[1] == '-n' and sys.argv[3] == '-s':
			val = int(sys.argv[2])
			for i in range(val):
				pid1 = os.fork()
				if pid1 == 0:
					parametre = sys.argv[4]
					arg = sys.argv[4:]
					os.execvp(parametre,arg)
				else:
					pid1, status = os.wait()
					if os.WIFEXITED(status):
						print("\tCode de sortie de la commande : {}".format(os.WEXITSTATUS(status)))
		
		elif sys.argv[1] == '-n':
			val = int(sys.argv[2])
			for i in range(val):
				pid2 = os.fork()
				if pid2 == 0:
					parametre = sys.argv[3]
					arg = sys.argv[3:]
					os.execvp(parametre,arg)
				else:
					os.wait()
				
		elif sys.argv[1] == '-s':
			pid3 = os.fork()
			if pid3 == 0:
				parametre = sys.argv[2]
				arg = sys.argv[2:]
				os.execvp(parametre,arg)
			else:
				pid3,status = os.wait()
				if os.WIFEXITED(status):
					print("\tCode de sortie de la commande : {}".format(os.WEXITSTATUS(status)))

		else:
			parametre = sys.argv[1]
			arg = sys.argv[1:]
			os.execvp(parametre,arg)

	else:
		pid, status = os.wait()
		if os.WIFEXITED(status):
			if sys.argv[1] == '-n':
				val = int(sys.argv[2])
				temp_fin = time.time()
				temp_ecoule = temp_fin - temp_debut
				durée_moyenne = temp_ecoule / val
				print("\tLa durée d'exécution en seconde : {} seconde(s)".format(temp_ecoule))
				print("\tLa durée d'exécution en microseconde : {} microseconde(s)".format(temp_ecoule * 1000000))
				print("\tLa durée moyenne d'exécution en seconde : {} seconde(s)".format(durée_moyenne))
			else:
				temp_fin = time.time()
				temp_ecoule = temp_fin - temp_debut
				print("\tLa durée d'exécution en seconde : {} seconde(s)".format(temp_ecoule))
				print("\tLa durée d'exécution en microseconde : {} microseconde(s)".format(temp_ecoule * 1000000))
	sys.exit(0)

	

	