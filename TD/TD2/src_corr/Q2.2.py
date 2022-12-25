import os, sys, time

if __name__ == '__main__':
    print("Je suis %d" % os.getpid())
    p = os.fork()
    if p == 0: # Fils
        print("fils %d de %d" % (os.getpid(), os.getppid()))
        time.sleep(5)
        sys.exit(12) 
    # Suite du père
    print("père %d de %d" % (os.getpid(), p))
    pid, status = os.wait()
    if os.WIFEXITED(status):
        print("Code sortie fils: %d" % os.WEXITSTATUS(status))
    else:
        print("child {} terminated abnormally".format(pid))
    sys.exit(0)

