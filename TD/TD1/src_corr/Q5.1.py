import os, sys

if __name__ == '__main__':
    print("Je suis %d" % os.getpid())
    p = os.fork()
    if p == 0: # fils 1
        print("fils1 %d de %d" % (os.getpid(), os.getppid()))
        sys.exit(0) # indispensable sinon le fils 1 fait le fork suivant !
    # Suite du père
    p = os.fork ()
    if p == 0: # fils 2
        print("fils2 %d du fils %d" % (os.getpid(), os.getppid()))
        sys.exit(0)
    # Suite du père
    sys.exit(0)
