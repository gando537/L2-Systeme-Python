import os,sys

fd = input("saisir au clavier : ")
s_bytes = fd.encode("utf-8")
rfd,wfd = os.pipe()
pid = os.fork()
if pid == 0:
	os.close(rfd)
	os.write(wfd,s_bytes)
	sys.exit(0)
else:
	os.wait()
	pid1 = os.fork()
	if pid1 == 0:
		os.close(wfd)
		saisi = os.read(rfd,len(fd))
		print("texte saisi : {}".format(saisi.decode("utf-8")))
sys.exit(0)