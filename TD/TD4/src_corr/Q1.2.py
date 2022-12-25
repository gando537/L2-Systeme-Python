import signal, sys, time

# La fonction qui sert de traitant au signal SIGALRM
def handler(sig, ignore):
    # Variable globale inaccessible sans cette declaration
    global counter
    counter += 1
    if counter < 6:
        # Les 5 premiere fois on affiche bip
        print("bip")
        # On reprogramme l’alarme pour la fois suivante
        signal.alarm(1)
    else:
        # La sixieme fois
        print("bye")
        sys.exit(0)

# on a besoin d’un compteur
counter = 0
# Met en place le traitant
signal.signal(signal.SIGALRM, handler)
# Programme l’arrivee du premier signal
signal.alarm(1)
# Se met en attente infinie
while (True):
    signal.pause()
