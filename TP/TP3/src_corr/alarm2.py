import signal, sys, time

def capter_INT(sig_num, frame):
    signal.alarm(5)

def capter_ALRM(sig_num, frame):
    print("Alarme !")
    sys.exit(0)

if __name__ == '__main__':
    signal.signal(signal.SIGINT, capter_INT)
    signal.signal(signal.SIGALRM, capter_ALRM)
    while True:
        time.sleep(1)
        print("Alive!")
