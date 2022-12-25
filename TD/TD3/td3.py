import os,sys,subprocess,shutil
# argv  = ["ls", "-lt"]
# os.execv("/bin/ls",argv)


# argv = sys.argv
# envp = os.environ
# if '/' not in argv[1]:
# 	chemin = shutil.which(argv[1])
# 	os.execve(chemin,argv[1:],envp)
# os.execve(argv[1],argv[1:],envp)

# sys.exit(0)

# ---------------------------- 2 Recouvrement -----------------------------------

argv = sys.argv
envp = os.environ
for i in range(1,len(argv)):
	if '/' not in argv[i]:
		chemin = shutil.which(argv[i])
		os.execve(chemin,argv[i:],envp)
	os.execve(argv[i],argv[i:],envp)

	sys.exit(0)

# ---------------------- 2 Recouvrement séquentiel-----------------------------------

# argv = sys.argv
# envp = os.environ
# for i in range(1,len(argv)):
# 	if '/' not in argv[i]:
# 		chemin = shutil.which(argv[i])
# 		os.execve(chemin,argv[i:],envp)
# 	os.execve(argv[i],argv[i:],envp)

# 	sys.exit(0)