import signal

def handler(sig, ignore):
    print("signal reçu = ", sig)

signal.signal(signal.SIGINT, handler)
signal.pause()

# chacune des deux lignes suivantes provoque une erreur:
# signal(signal.SIGKILL, handler)
# signal.signal(signal.SIGSTOP, handler)
#
# en effet, on ne peut pas redefinir le handler de SIGKILL et SIGSTOP
# Ces signaux provoquent la terminaison/la suspension du programme

