import os, sys, time

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("Usage : %s nbsec sig com [arg ...]" % sys.argv[0], file=sys.stderr)
        sys.exit(1)
    nbsec = float(sys.argv[1])
    sig = int(sys.argv[2])
    print("Père %d" % os.getpid())        
    p = os.fork()        
    if p == 0:  # Fils
        print("Fils %d" % os.getpid())
        # Recouvrement
        try:
            os.execvp(sys.argv[3], sys.argv[3:])
        except FileNotFoundError:
            print("Impossible de trouver le fichier %s" % sys.argv[3])
            sys.exit(1)
        except PermissionError:
            print("Le fichier %s existe mais vous n'avez pas les bonnes permissions" % sys.argv[3])
            sys.exit(2)
    # Suite père 
    time.sleep(nbsec)
    print("Père envoie signal %d à %d" % (sig, p))
    os.kill(p, sig)
    os.wait()  # Pour lever le zombie
    print("Père détecte fin du fils")
    sys.exit(0)
