import os, signal, sys

if __name__ == '__main__':    
    print("Père %d" % os.getpid())
    p = os.fork()
    if p == 0: # Fils
        print("Fils %d" % os.getpid())
        os.kill(os.getppid(), signal.SIGUSR1)
        sys.exit(0)
    # Suite père
    print("Père: attente fin fils")
    os.wait()
    sys.exit(0)
