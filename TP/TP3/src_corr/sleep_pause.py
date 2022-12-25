import os, signal, time

def traitant(s, _):
    print("signal", s, "capté")

signal.signal(signal.SIGINT, traitant)
print(os.getpid())
#time.sleep(30)
signal.pause()

# signal.pause(): à la réception d'un signal: termine.
# time.sleep(n):
# - Python 3.4- : à la reception d'un signal: termine => on n'est jamais 
# assuré de dormir n secondes.
# - Python 3.5+ : à la reception d'un signal, exécute le traitant associé et 
# poursuit son sommeil => on est assuré de dormir au moins n secondes.
