#! /usr/bin/env python
# file: client.py (module client)
import sys,os
 # tube pere vers fils
# tube pere vers fils
def client(readfd, writefd):
	global MAXLINE
	nomfic = input("entrez un nom de fichier : ")
	os.write(writefd, nomfic.encode("utf-8")) # envoyer nom fichier 
	# lire contenu du fichier sur tube depuis serveur 
	buff = os.read(readfd, MAXLINE)
	while len(buff) > 0 :
		os.write(1, buff) # ecrire contenu du fichier sur sortie standard 
		buff = os.read(readfd, MAXLINE)