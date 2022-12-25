import os, sys

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("Usage: %s com arg1 ... argn" % sys.argv[0], file=sys.stderr)
        sys.exit(1)
    p = os.fork()
    if p == 0: # Fils
        try:
            os.execvp(sys.argv[1], sys.argv[1:])
        except FileNotFoundError:
            print("Erreur lors du chargement de %s" % sys.argv[1], file=sys.stderr)
            sys.exit(13)
    # Suite du père
    pid, status = os.wait()
    if os.WIFEXITED(status):
        if os.WEXITSTATUS(status) == 0:
            print("Processus %d terminé: succès" % p)
        else: 
            print("Processus %d terminé: échec (code erreur: %d)" \
                % (p, os.WEXITSTATUS(status)))
    sys.exit(0)

