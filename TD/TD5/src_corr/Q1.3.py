import os, signal, sys, time

def capter(sig, frame):
    print("Père: SIGUSR1 reçu")

if __name__ == '__main__':    
    if len(sys.argv) < 2:
        print("Erreur: argument attendu", file=sys.stderr)
        sys.exit(1)
    n = int(sys.argv[1])
    print("Père %d" % os.getpid())
    p = os.fork()
    if p == 0: # Fils
        print("Fils %d" % os.getpid())
        for i in range(n):
            os.kill(os.getppid(), signal.SIGUSR1)
        sys.exit(0)
    # Suite père
    signal.signal(signal.SIGUSR1, capter)
    print("Père: attente fin fils")
    os.wait()
    sys.exit(0)
