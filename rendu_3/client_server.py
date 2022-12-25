import os, sys,signal,atexit

_MAXBYTES = 1000

_SEPARATOR = ' '

def server(readfd, writefd):
	buff = os.read(readfd, _MAXBYTES)
	while len(buff) > 0:
		os.write(writefd, buff)
		buff = os.read(readfd, _MAXBYTES)

def client(readfd, writefd):
	while True:
		inputbuff = os.read(0, _MAXBYTES)            # lire contenu depuis entrée standard
		os.write(writefd,inputbuff)                 # envoyer contenu sur tube vers serveur
		if len(inputbuff) == 0:
			break
		buff = os.read(readfd, _MAXBYTES)            #lire reponse serveur
		if len(buff) == 0:
			break
		os.write(1, buff)                            # ecrire contenu du fichier sur sortie standard




