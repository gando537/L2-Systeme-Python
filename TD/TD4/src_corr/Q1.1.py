import signal, sys, time

def handler(sig, ignore):
    print("interruption")
    sys.exit(0)

# Met en place le nouveau traitant
signal.signal(signal.SIGINT, handler)

time.sleep(float(sys.argv[1]))
sys.exit(0)
