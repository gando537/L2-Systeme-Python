import os, sys

MAXLINE = 1000

def client(readfd, writefd):
   nomfic = input("entrez un nom de fichier : ")
   os.write(writefd, nomfic.encode('utf-8'))   # envoyer nom fichier sur tube vers serveur
   # lire contenu du fichier sur tube depuis serveur
   buff = os.read(readfd, MAXLINE)
   while len(buff) > 0:
       os.write(1, buff)  # ecrire contenu du fichier sur sortie standard
       buff = os.read(readfd, MAXLINE)


wfd1 = os.open("/tmp/ma_fifo1", os.O_WRONLY) # ouvre fifo1 en ecriture
rfd2 = os.open("/tmp/ma_fifo2", os.O_RDONLY) # ouvre fifo2 en lecture
client(rfd2, wfd1)          # pere execute client
sys.exit(0)
