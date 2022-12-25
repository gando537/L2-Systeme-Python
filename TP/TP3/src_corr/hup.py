import os, signal, time

print(os.getpid())
signal.signal(signal.SIGHUP, signal.SIG_IGN)
time.sleep(60)
