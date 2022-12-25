import os, sys

if __name__ == '__main__':
    print("Je suis %d" % os.getpid())
    p = os.fork()
    if p == 0: # fils
        print("fils %d de %d" % (os.getpid(), os.getppid()))
        p = os.fork ()
        if p == 0: # petit-fils
            print("petit-fils %d de %d" % (os.getpid(), os.getppid()))
            sys.exit(0)
        # Suite du fils
        sys.exit(0)
    # Suite du père
    sys.exit(0)
