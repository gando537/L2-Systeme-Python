import os, signal, sys

def capter_fils(sig, frame):
    global i
    print("Fils: SIGUSR1 reçu")
    i += 1
    if i >= n:
        sys.exit(0)
    os.kill(os.getppid(), signal.SIGUSR1)

def capter_pere(sig, frame):
    print("Père: SIGUSR1 reçu")
    os.kill(p, signal.SIGUSR1)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Erreur: argument attendu", file=sys.stderr)
        sys.exit(1)
    n = int(sys.argv[1])
    print("Père %d" % os.getpid());
    p = os.fork()
    if p == 0: # Fils        
        i = 0
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
