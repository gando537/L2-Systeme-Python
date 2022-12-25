import os,sys


fd = input("saisir du texte au clavier : ")
x = fd.encode('utf-8')

rfd,wfd = os.pipe()
pid = os.fork()
if pid == 0:
	os.close(wfd)
	d_rfd = os.dup(rfd)
	c = os.read(d_rfd,len(fd))
	print("Texte saisi au clavier : {}".format(c.decode("utf-8")))
	os.close(d_rfd)
	os.execv('/bin/cat',['/bin/cat'])
	
else:
	
	os.close(rfd)
	d_wfd = os.dup(wfd)
	os.write(d_wfd,x)
	os.close(d_wfd)
	os.execv('/bin/cat',['/bin/cat'])
sys.exit(0)












