import os,sys

MAXLINE = 1000

def server(readfd,writefd):
	global MAXLINE
	buff = os.read(readfd,MAXLINE)
	try:
		fd = os.open(buff,os.O_RDONLY)
	except:
		os.write(writefd, b"error : can't open" + buff + b'\n')

	else:
		# Ouverture réussie
		buff = os.read(fd,MAXLINE)
		while len(buff)>0:
			os.write(writefd, buff)
			buff = os.read(fd, MAXLINE)
		os.close(fd)