import os

MAXBYTES = 1000

def child():
    os.close(wfd1)
    os.close(0)
    os.dup(rfd1)
    os.close(rfd1)
    buff = os.read(0, MAXBYTES)
    while len(buff) > 0:
       os.write(1, buff)  # écrire contenu du l'entrée std sur la sortie std
       buff = os.read(0, MAXBYTES)

def father():
    os.close(rfd1)
    os.close(1)
    os.dup(wfd1)
    os.close(wfd1)
    buff = os.read(0, MAXBYTES)
    while len(buff) > 0:
       os.write(1, buff)  # écrire contenu du l'entrée std sur la sortie std
       buff = os.read(0, MAXBYTES)

if __name__ == '__main__':
    rfd1, wfd1 = os.pipe() # tube père vers fils
    childpid = os.fork()
    if childpid == 0: # child
        child()
    else: # father
        father()
