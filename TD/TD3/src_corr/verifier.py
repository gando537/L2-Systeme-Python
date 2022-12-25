import os, sys

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("Usage: %s com arg1 ... argn" % sys.argv[0], file=sys.stderr)
        sys.exit(1)
    try:
        os.execvp(sys.argv[1], sys.argv[1:])
    except FileNotFoundError:
        print("Erreur lors du chargement de %s" % sys.argv[1], file=sys.stderr)
        sys.exit(2)

