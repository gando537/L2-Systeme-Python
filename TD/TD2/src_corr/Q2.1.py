import os, sys, time

if __name__ == '__main__':
    print("Je suis %d" % os.getpid())
    p = os.fork()
    if p == 0: # Fils
        print("fils %d de %d" % (os.getpid(), os.getppid()))
        time.sleep(5)
        sys.exit(0) 
    # Suite du père
    print("père %d de %d" % (os.getpid(), p))
    os.wait()
    print("Mon fils est mort")
    sys.exit(0)

