import os, signal, sys, time

def capter(sig, frame):
    global nsig
    nsig += 1

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
    nsig = 0
    signal.signal(signal.SIGUSR1, capter)
    print("Père: attente fin fils")
    os.wait()
    print("Père: %d SIGUSR1 reçus" % nsig)
    sys.exit(0)
