import os,sys


fd = input("saisir un texte au clavier : ")
x = fd.encode('utf-8')
rfd,wfd = os.pipe()
pid = os.fork()
if pid == 0:
	os.close(wfd)
	c = os.read(rfd,len(fd))
	print("Texte saisi au clavier : {}".format(c.decode("utf-8")))
else:
	os.close(rfd)
	os.write(wfd,x)
	sys.exit(0)

