import os, sys, time

if __name__ == '__main__':
    print("Je suis %d" % os.getpid())
    
    while True:
        time.sleep(2)
        p = os.fork()
        if p != 0:
            sys.exit(0)  # père
        # Suite du fils
        print("Je suis maintenant %d" % os.getpid())
    sys.exit(0)
