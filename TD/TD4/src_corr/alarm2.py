import os, signal, sys

def ALRM_handler(sig_num, frame):
    signal.alarm(1)           # Relancer l'alarme
    try:
        os.kill(pid_pere, 0)
    except OSError:
        print("Fils détecte fin père")
        sys.exit(0)
    
if __name__ == '__main__':
    pid_pere = os.getpid()
    print("Père %d" % pid_pere)
    p = os.fork()
    if p == 0: # Fils
        print("Fils %d" % os.getpid())
        signal.signal(signal.SIGALRM, ALRM_handler)
        signal.alarm(1)
        while True:
            pass  # Pour maintenir le fils en vie
        sys.exit(0)
    
    # Suite père
    bytes = os.read(0, 1)
    while len(bytes) != 0:
        os.write(1, bytes)
        bytes = os.read(0, 1)
    sys.exit(0)
