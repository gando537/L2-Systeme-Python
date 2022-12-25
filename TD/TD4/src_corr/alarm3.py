import os, sys, time

if __name__ == '__main__':
    pid_pere = os.getpid()
    print("Père %d" % pid_pere)
    p = os.fork()
    if p == 0: # Fils
        print("Fils %d" % os.getpid())
        while True:
            time.sleep(1)
            try:
                os.kill(pid_pere, 0)
            except OSError:
                print("Fils détecte fin père")
                break
        sys.exit(0)
    # Suite père
    bytes = os.read(0, 1)
    while len(bytes) != 0:
        os.write(1, bytes)
        bytes = os.read(0, 1)
    sys.exit(0)
