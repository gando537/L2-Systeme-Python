import os

def child():
    os.close(wfd1) # le fils n'écrit pas dans le pipe
    os.dup2(rfd1, 0) # 0 et rfd1 pointent vers la sortie du pipe
    os.close(rfd1) # on n'a plus besoin de rfd1
    os.execv('/bin/cat', ['/bin/cat'])
    print("something went wrong")

def father():
    os.close(rfd1) # le père ne lit pas depuis le pipe
    os.dup2(wfd1, 1) # 1 et wfd1 pointent vers l'entrée du pipe
    os.close(wfd1) # on n'a plus besoin de wfd1
    os.execv('/bin/cat', ['/bin/cat'])
    print("something went wrong")

if __name__ == '__main__':
    rfd1, wfd1 = os.pipe() # tube père vers fils
    childpid = os.fork()
    if childpid == 0: # child
        child()
    else: # father
        father()
