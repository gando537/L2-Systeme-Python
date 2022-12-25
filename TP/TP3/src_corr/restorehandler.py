import signal, time

def capter_INT(sig_num, frame):
    signal.signal(signal.SIGINT, original_sigint_handler)
    print("Ouch!")

if __name__ == '__main__':
    original_sigint_handler = signal.getsignal(signal.SIGINT)
    signal.signal(signal.SIGINT, capter_INT)
    while True:
        time.sleep(1)
        print("Alive!")

# la ligne 4 peut être remplacée par signal.signal(signal.SIGINT, signal.SIG_DFL)
# auquel cas, la ligne 8 n'a plus lieu d'être.
