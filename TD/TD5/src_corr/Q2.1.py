import os, signal, sys

def capter_fils(sig, frame):
    print("Fils: SIGUSR1 reçu")        
    sys.exit(0)

def capter_pere(sig, frame):
    print("Père: SIGUSR1 reçu")
    os.kill(p, signal.SIGUSR1)

if __name__ == '__main__':
    print("Père %d" % os.getpid());
    p = os.fork()
    if p == 0: # Fils        
        print("Fils %d" % os.getpid())
        signal.signal(signal.SIGUSR1, capter_fils)
        os.kill(os.getppid(), signal.SIGUSR1)
        while True:
            signal.pause() # Maintient en vie
        sys.exit(0)
    # Suite père
    signal.signal(signal.SIGUSR1, capter_pere)
    print("Père: attente fin fils")
    os.wait()
    print("Père: fin fils")
    sys.exit(0)
