import atexit, signal, sys, time

def onexit():
    print("bye")

def handler(s, _):
    sys.exit(0)

atexit.register(onexit)
for s in [signal.SIGINT, signal.SIGQUIT, signal.SIGABRT, signal.SIGTERM]:
    signal.signal(s, handler)
time.sleep(60)
if len(sys.argv) > 1:
    sys.exit(1)
sys.exit(0)
