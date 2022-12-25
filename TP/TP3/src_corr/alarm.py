import signal, sys, time

def capter_ALRM(sig_num, frame):
    print("Alarme !")
    sys.exit(0)

if __name__ == '__main__':
    signal.signal(signal.SIGALRM, capter_ALRM)
    signal.alarm(10)
    while True:
        time.sleep(1)
        print("Alive!")
