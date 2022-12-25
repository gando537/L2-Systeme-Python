import os, signal, sys

compteur = 0  # variable globale

def ALRM_handler(sig_num, frame):
    global compteur
    signal.alarm(2)                # Relancer l'alarme
    compteur += 1
    print(compteur)
    if compteur == 5:
        sys.exit(0)

if __name__ == '__main__':
    signal.signal(signal.SIGALRM, ALRM_handler)
    signal.alarm(2)
    bytes = os.read(0, 1)
    while len(bytes) != 0:
        os.write(1, bytes)
        bytes = os.read(0, 1)
    sys.exit(0)
