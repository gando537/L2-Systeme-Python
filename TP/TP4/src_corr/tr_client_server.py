import os, sys

_MAXBYTES = 1000

def _tr(buf, entree, sortie):
    s = buf.decode('utf-8')
    s = s.translate(str.maketrans(entree, sortie))
    return s.encode('utf-8')

def server(readfd, writefd, entree, sortie):
    buff = os.read(readfd, _MAXBYTES)
    while len(buff) > 0:
        buff = _tr(buff, entree, sortie)
        os.write(writefd, buff)
        buff = os.read(readfd, _MAXBYTES)

def client(readfd, writefd):
    while True:
       inputbuff = os.read(0, _MAXBYTES) # lire contenu depuis entrée standard
       if len(inputbuff) == 0:
            break
       os.write(writefd, inputbuff)      # envoyer contenu sur tube vers serveur
       buff = os.read(readfd, _MAXBYTES) #lire reponse serveur
       if len(buff) == 0:
            break
       os.write(1, buff)  # ecrire contenu du fichier sur sortie standard



