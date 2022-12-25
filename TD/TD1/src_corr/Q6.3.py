import os, sys

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: %s <int>" % sys.argv[0], file=sys.stderr)
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print('''Can't convert "%s" to int''' % sys.argv[1], file=sys.stderr)
        sys.exit(2)
    print("Père pid = %d" % os.getpid())
    for i in range(n):
        p = os.fork()
        if p == 0:  # Fils i
            print("Fils %d, pid = %d" % (i+1, os.getpid()))
            sys.exit(0)  # important !!
        # Suite père
    sys.exit(0)
