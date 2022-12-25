import os, signal, sys, time

def handler(sig, ignore):
    global counter
    pid = 1 # pour amorcer la boucle while
    try:
        while pid > 0 and counter > 0:
            pid, status = os.waitpid(-1, os.WNOHANG)
            if pid > 0:
                print("père: fils %d terminé" % pid)
                counter -= 1
                print("Nombre de fils restants: %d" % counter)
    except OSError:
        pass
if __name__ == "__main__":
    signal.signal(signal.SIGCHLD, handler)
    counter = max_fils = 5
    # compte le nombre de fils restant
    # boucle de 0 a max_fils-1
    for i in range(max_fils):
        if os.fork() == 0:
            # le fils i
            print("fils {} (pid={}) terminé".format(i, os.getpid()))
            sys.exit(0)
    # ici le père peut travailler sur autre chose sans se soucier
    # de ses fils. Il fait semblant en faisant une boucle vide.
    while counter > 0:
        pass
    print("père: Tous mes fils sont terminés.")
    sys.exit(0)
    # Attention, petite faiblesse de python par raport à C:
    # vous risquez d'avoir lors de certaines exécutions:
    # RuntimeError: reentrant call inside <_io.BufferedWriter name='<stdout>'>
    # Cela provient des print() du handler qui ne sont pas réentrant.
    # i.e. un print() n'est pas terminé, alors que le handler est appelé de nouveau
    # ce qui provoque un print() au milieu d'un print().
    # Il faut trouver un astuce pour ne pas faire de print() dans les handlers.
