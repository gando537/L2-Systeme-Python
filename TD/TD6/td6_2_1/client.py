import os,sys

MAXLINE = 1000

def client(readfd,writefd):
	global MAXLINE
	nom_fichier = input("Entrez un nom de fichier : ")
	os.write(writefd,nom_fichier.encode("utf-8"))			# Envoyez nom_fichier sur tube vers server
	buff = os.read(readfd, MAXLINE)							# Lire contenu du fichier sur tube depuis server
	while len(buff) > 0:
		os.write(1, buff)									# Ecrire contenu du tube sur la sortie standard
		buff = os.read(readfd, MAXLINE)