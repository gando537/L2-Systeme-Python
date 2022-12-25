import os, sys

if __name__ == '__main__':
    print("Père pid = %d" % os.getpid())
    for i in range(3):
        p = os.fork()
        if p == 0: # Fils i
            print("Fils %d, pid = %d" % (i, os.getpid()))
            for j in range(2):
                p = os.fork()
                if p == 0: # Petit-fils j
                    print("Petit-fils %d de %d, pid=%d"% (j, i, os.getpid()))
                    sys.exit(0)
                # Suite fils i
            sys.exit(0)
        # Suite père
    sys.exit(0)
