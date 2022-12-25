import os,sys


fd = input("saisir quelque chose : ")
x = fd.encode('utf-8')

rfd,wfd = os.pipe()
pid = os.fork()
if pid == 0:
	os.close(wfd)
	d_rfd = os.dup(rfd)
	c = os.read(d_rfd,len(fd))
	print("\tTexte saisi : {}".format(c.decode("utf-8")))
	os.close(d_rfd)
	os.execv('/bin/cat',['cat'])
	
else:
	
	os.close(rfd)
	d_wfd = os.dup(wfd)
	os.write(d_wfd,x)
	os.close(d_wfd)
	os.execv('/bin/cat',['cat'])
sys.exit(0)


# La création d’un tube correspond à celle de deux descripteurs de fichiers, l’un permettant d’écrire dans le tube, 
# l’autre d’y lire par les opérations read et write.

# desc[0] est la sortie du tube, i.e. le numéro du descripteur pour la lecture (mnémonique : 0 est l’entrée standard) ;
# desc[1] est l’entrée du tube, i.e. le numéro du descripteur pour l’écriture (mnémonique : 1 est la sortie standard) ;
# la valeur de retour est 0 si la création s’est bien passée et −1 en cas de problème.












