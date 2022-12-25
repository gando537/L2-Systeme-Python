import os, sys

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("Usage : %s nbsec sig com [arg ...]" % sys.argv[0], file=sys.stderr)
        sys.exit(1)
    nbsec = int(sys.argv[1])
    sig = int(sys.argv[2])

    # Recouvrement
    try:
        os.execvp(sys.argv[3], sys.argv[3:])
    except FileNotFoundError:
        print("Impossible de trouver le fichier %s" % sys.argv[3])
        sys.exit(1)
    except PermissionError:
        print("Le fichier %s existe mais vous n'avez pas les bonnes permissions" % sys.argv[3])
        sys.exit(2)
