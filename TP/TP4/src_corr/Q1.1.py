import os

MAXBYTES = 1000

def child():
    os.close(wfd1)
    buff = os.read(rfd1, MAXBYTES)
    while len(buff) > 0:
       os.write(1, buff)  # écrire contenu du tube sur la sortie standard
       buff = os.read(rfd1, MAXBYTES)

def father():
    os.close(rfd1)
    buff = os.read(0, MAXBYTES)
    while len(buff) > 0:
       os.write(wfd1, buff)  # écrire contenu de l'entrée standard sur le tube
       buff = os.read(0, MAXBYTES)

if __name__ == '__main__':
    rfd1, wfd1 = os.pipe() # tube père vers fils
    childpid = os.fork()
    if childpid == 0: # child
        child()
    else: # father
        father()
