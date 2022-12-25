import os,sys

def indice(liste,element):
	return liste.index(element)

max_bytes = 1000


def client(readfd, writefd):
	global max_bytes
	arguments = sys.argv[1:]
	for arg in arguments:
		if indice(arguments,arg) == len(arguments) - 1: 
			arg = arg + ' '
		else:
			arg = arg
		os.write(writefd, arg.encode("utf-8")) 
	buff = os.read(readfd, max_bytes)
	while len(buff) > 0 :
		os.write(1, buff)
		buff = os.read(readfd, max_bytes)

def server(readfd, writefd):

	global max_bytes
	buff = os.read(readfd, max_bytes)
	buff1 = buff.decode("utf-8")
	len_chaine_1 = int(len(buff1) / 2)
	chaine_1 = buff1[:len_chaine_1]
	chaine_2 = buff1[len_chaine_1:]
	mot = buff1.split()
	nuk = buff1.replace(chaine_1,chaine_2)
	try:
		fd = os.open(nuk, os.O_RDONLY) 
	except:
		os.write(writefd,nuk.encode("utf-8")) 
		sys.exit(1)
	nuk = os.read(fd, max_bytes)
	while (nuk.len > 0):
		os.write(writefd,nuk.encode("utf-8"))
		nuk = os.read(fd, max_bytes)
	os.close(fd)

if __name__ == '__main__':

	if len(sys.argv[1]) != len(sys.argv[2]):
		print("Usage : entree et sortie doivent avoir la même longueur")
		sys.exit(0)

	os.mkfifo("/tmp/fifo1")
	os.mkfifo("/tmp/fifo2")
	childpid = os.fork()
	if childpid == 0:
		rfd1 = os.open("/tmp/fifo1", os.O_RDONLY)
		wfd2 = os.open("/tmp/fifo2", os.O_WRONLY)
		server(rfd1, wfd2)     
		sys.exit(0)
	wfd1 = os.open("/tmp/fifo1", os.O_WRONLY) 
	rfd2 = os.open("/tmp/fifo2", os.O_RDONLY) 
	client(rfd2, wfd1)          
	os.waitpid(childpid, 0)           
	os.unlink("/tmp/fifo1")         
	os.unlink("/tmp/fifo2")
	print("")
	sys.exit(0)