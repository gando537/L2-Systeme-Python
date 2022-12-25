import os, sys

if __name__ == '__main__':
    print("Père pid = %d" % os.getpid())
    for i in range(5):
        p = os.fork()
        if p == 0:  # Fils i
            print("Fils pid = %d" % os.getpid())
            sys.exit(0)  # important !!
        # Suite père
    sys.exit(0)
