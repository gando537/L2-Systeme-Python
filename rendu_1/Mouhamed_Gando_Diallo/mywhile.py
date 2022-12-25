import os, sys, time, signal

def indice(liste,element):
	return liste.index(element)

if __name__ == '__main__':



	commandes = []
	for i in range(1,len(sys.argv)):
		if '-' in sys.argv[i]:
			pass
		else:
			args = []
			if i != len(sys.argv) - 1 and '-' in sys.argv[i+1]:
				args.append(sys.argv[i])
				for j in range(i+1,len(sys.argv)):
					if sys.argv[j] == '--do' or sys.argv[j] == '--done':
						break
					elif '-' in sys.argv[j]:
						args.append(sys.argv[j])
					else :
						break
				commandes.append((args[0],args))
			else:
				commandes.append((sys.argv[i],[sys.argv[i]]))

	arguments = sys.argv[1:]
	indice_do = indice(arguments,'--do')
	indice_done = indice(arguments, '--done')
	command1 = arguments[0]
	indice_command1 = indice(arguments,command1)
	command2 = arguments[indice_do + 1]
	indice_command2 = indice(arguments,command2)
	x = len(arguments) - 1
	if indice_do < 1 or indice_do > indice_command2 or indice_done != x:
		print("Usage: {} command1 [arg ...] --do command2 [arg ...] --done".format(sys.argv[0], file=sys.stderr))
		sys.exit(1)

	else:
		
		pid = os.fork()
		if pid == 0:
			while True:
				pid1 = os.fork()
				if pid1 == 0:
					try:
						comd1,arg = commandes[0]
						os.execvp(comd1, arg)
						 
					except FileNotFoundError:
						print("Erreur lors du chargement de {}".format(sys.argv[1], file=sys.stderr))
						sys.exit(2)
				else:
					os.wait()
					pid2 = os.fork()
					if pid2 == 0:
						try:
							comd2,arg = commandes[1]
							os.execvp(comd2, arg)
						except FileNotFoundError:
							print("Erreur lors du chargement de {}".format(sys.argv[1], file=sys.stderr))
							sys.exit(2)
					else:
						os.wait()


		else:
			pid,status = os.wait()

			if os.WIFEXITED(status):
				print("\tCode de sortie de la commande_2 : {}".format(os.WEXITSTATUS(status)))
			
			
			

				