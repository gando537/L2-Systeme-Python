import os,sys,time

#print(os.getpid())
#print(os.getppid())


#----------------------------- Q 3.1 ----------------------------------


# print(" Père = {} et fils = {}".format(os.getppid(),os.getpid()))
# pid = os.fork()

# if pid == 0 :
# 	print(" Fils 1 : Père = {} et moi = {}".format(os.getppid(),os.getpid()))
# 	for i in range(1,3):
# 		pid = os.fork()
# 		if pid == 0 :
# 			print(" Petit-fils {} : Père = {} et moi = {}".format(i,os.getppid(),os.getpid()))
# 			sys.exit(0)
# else :
# 	for i in range(2,4):
# 		pid = os.fork()
# 		if pid == 0 :
# 			print(" Fils {} : Père = {} et moi = {}".format(i,os.getppid(),os.getpid()))
# 			sys.exit(0)
#----------------------------- OU ----------------------------------


# def afficher(msg) : print("{} ; Père = {} et moi = {}".format(msg,os.getppid(),os.getpid()))

# pid = os.fork()
# if pid == 0:

# 	afficher(" fils 1")
# 	pid = os.fork()
# 	if pid == 0 :
# 		afficher(" Petit-fils 1")
# 		sys.exit(0)
# 	else :
# 		pid = os.fork()
# 		if pid == 0 :
# 			afficher(" Petit-fils 2")
# 			sys.exit(0)

# else :
# 	pid1 = os.fork()
# 	if pid1 == 0:
# 		afficher(" fils 2")
# 		sys.exit(0)
# 	else : 
# 		pid = os.fork()
# 		if pid == 0:
# 			afficher(" fils 3")
# 			sys.exit(0)

#----------------------------- Q 3.3 ----------------------------------

#chaine

# parametre = int(sys.argv[1])
# print(parametre)
# print("pid = %d, ppid = %d" % (os.getpid(), os.getppid()))
# for i in range(parametre):
# 	pid_fils = os.fork()
# 	if pid_fils == 0:
# 		print("pid = %d, ppid = %d" % (os.getpid(), os.getppid()))
# 		sys.exit(0)



# #arbre

# parametre = int(sys.argv[1])
# print(parametre)
# print("pid = %d, ppid = %d" % (os.getpid(), os.getpid()))
# for i in range(parametre):
# 	if os.fork() == 0:
# 		print("pid = %d, ppid = %d" % (os.getpid(), os.getppid()))
# 	else :
# 		sys.exit(0)



#---------------------------------------------------------------



# pid = os.fork()
# if (pid != 0):
# 	print ("je suis le père %d, j'attends mon fils" % (os.getpid()))
# 	(fils,statut) = os.wait()
# 	if (os.WIFEXITED(statut)):
# 		print ("%d : mon fils %d s'est terminé avec le code %d" % (os.getpid(), fils, os.WEXITSTATUS(statut)))
# 		sys.exit(0)
# else:
# 	print ("je suis le fils, mon PID est %d" % (os.getpid()))
# 	time.sleep(2)
# 	print ("fin du fils")
# 	sys.exit(1)


# pid = os.fork()
# if (pid == 0):
# 	os.execl("/bin/ls", "-a")
# else:
# 	os.wait()
# sys.exit(0)

# import signal
# def handler(sig,frame):
# 	print("\nLe signal est bien reçu !")
# 	sys.exit(0)



# signal.signal(signal.SIGINT,handler)
# signal.pause()
# sys.exit(0)

# import signal
# def handler(sig,frame):
# 	print("\nTrop tard le temps est écoulé !")
# 	sys.exit(0)

# signal.signal(signal.SIGALRM,handler)
# signal.alarm(5)
# reponse = input("Entrez un nombre avant 5 sec. : ")
# signal.alarm(0)
# print("bien reçu !")
# sys.exit(0)


# #---------------------------------------------------------------

# pid = os.fork()
# if (pid != 0):
# 	print("je suis le père %d, j'attends mon fils" % (os.getpid()))
# 	(fils,statut) = os.wait()
# 	if os.WIFEXITED(statut):
# 		print("%d : mon fils %d s'est terminé avec le code %d" %(os.getpid(), fils, os.WEXITSTATUS(statut)))
# 	sys.exit(0)
# else:
# 	print("je suis le fils, mon PID est %d" % (os.getpid()))
# 	time.sleep(2)
# 	print("fin du fils")
# 	sys.exit(1)


# def switch_demo(argument):
#     switcher = {
#         1: "January",
#         2: "February",
#         3: "March",
#         4: "April",
#         5: "May",
#         6: "June",
#         7: "July",
#         8: "August",
#         9: "September",
#         10: "October",
#         11: "November",
#         12: "December"
#     }
#     print (switcher.get(argument, "Invalid month"))

# print(switch_demo(3))

# #----------------------------- Q 4.2 ----------------------------------

# def afficher(msg) : print("{} ; Père = {} et moi = {}".format(msg,os.getppid(),os.getpid()))

# pid = os.fork()
# if pid == 0:

# 	afficher(" fils 1")
# 	pid = os.fork()
# 	if pid == 0 :
# 		afficher(" Petit-fils 1")
# 		sys.exit(0)
# 	else :
# 		pid = os.fork()
# 		if pid == 0 :
# 			afficher(" Petit-fils 2")
# 			sys.exit(0)

# else :
# 	os.wait()
# 	pid1 = os.fork()
# 	if pid1 == 0:
# 		afficher(" fils 2")
# 		sys.exit(0)
# 	else : 
# 		pid = os.fork()
# 		if pid == 0:
# 			afficher(" fils 3")
# 			sys.exit(0)

# #----------------------------- Q 5.2 ----------------------------------

# import os,sys,subprocess,shutil
# # argv  = ["ls", "-lt"]
# # os.execv("/bin/ls",argv)


# argv = sys.argv
# envp = os.environ
# if '/' not in argv[1]:
# 	chemin = shutil.which(argv[1])
# 	os.execve(chemin,argv[1:],envp)

# os.execve(argv[1],argv[1:],envp)

# sys.exit(0)
















