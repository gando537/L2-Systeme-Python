import os, signal, sys

def capter(sig, frame):
    print("Père: SIGUSR1 reçu")

if __name__ == '__main__':    
    print("Père %d" % os.getpid())
    p = os.fork()
    if p == 0: # Fils
        print("Fils %d" % os.getpid())
        os.kill(os.getppid(), signal.SIGUSR1)
        sys.exit(0)
    # Suite père
    signal.signal(signal.SIGUSR1, capter)
    print("Père: attente fin fils")
    os.wait()
    sys.exit(0)
