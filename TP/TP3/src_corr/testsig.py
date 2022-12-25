import signal, time

def capter_INT(sig_num, frame):
    print("Ouch!")

signal.signal(signal.SIGINT, capter_INT)
while True:
    time.sleep(1)
    print("Alive!")
