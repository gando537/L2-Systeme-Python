import sys, os

def indice(liste,element):
	return liste.index(element)

if __name__ == '__main__':


	commande = []
	for i in range(1,len(sys.argv)):
		if '-' in sys.argv[i] :
			pass
		else:
			args = []
			if i != len(sys.argv) - 1 and '-' not in sys.argv[i+1]:
				args.append(sys.argv[i])
				for j in range(i+1,len(sys.argv)):
					if sys.argv[j] != '--then' and sys.argv[j] != '--else' and sys.argv[j] != '--fi':
						args.append(sys.argv[j])
					else :
						break
				commande.append((args[0],args))
			else:
				commande.append((sys.argv[i],[sys.argv[i]]))
				
	arguments = sys.argv[1:]
	indice_then = indice(arguments,'--then')
	indice_else = indice(arguments, '--else')
	indice_fi = indice(arguments, '--fi')
	command1 = arguments[0]
	indice_command1 = indice(arguments,command1)
	command2 = arguments[indice_then + 1]
	indice_command2 = indice(arguments,command2)
	command3 = arguments[indice_else + 1]
	indice_command3 = indice(arguments,command3)
	commandes = [command1,command2,command3]

	for i in range(len(commandes)):
		if commandes[i] == '--then' or commandes[i] == '--else' or commandes[i] == '--fi':
			print("Usage: {} command1 arg ... --then command2 arg ... [ --else command3 arg ...] --fi".format(sys.argv[0], file=sys.stderr))
			sys.exit(1)

	pid = os.fork()
	if pid == 0:
		comm1,arg1 = commande[0]
		os.execvp(comm1,arg1)
	else:
		pid, status = os.wait()
		if os.WIFEXITED(status):
			if os.WEXITSTATUS(status) == 0:
				comm2,arg2 = commande[1]
				os.execvp(comm2,arg2)
			else:
				comm3,arg3 = commande[2]
				os.execvp(comm3,arg3)
		sys.exit(0)