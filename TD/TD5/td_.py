import os,sys

fd =os.open("toto.txt", os.O_RDONLY)
pid = os.fork()
if pid == 0 :
	c = os.read(fd, 1)
	sys.exit(0)
os.wait()
c = os.read(fd, 1)
print("c = {}".format(c))
sys.exit(0)

#----------------------------------------------------------------

# le fichier toto.txt contenant que la chaine "lambda" ce programme va afficher
# le deuxième caractère qu'est la lettre 'a'