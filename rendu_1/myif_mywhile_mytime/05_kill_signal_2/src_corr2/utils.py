import os, sys

def execvp_with_exception_handling(com, argv):
    try:
        os.execvp(com, argv)
    except FileNotFoundError:
        print("%s: no such command: %s" % \
            (sys.argv[0], sys.argv[1]), file=sys.stderr)
        sys.exit(2)
    except PermissionError:
        print("%s: can't execute: %s" % \
            (sys.argv[0], sys.argv[1]), file=sys.stderr)
        sys.exit(13)

def indice(liste, element, start):
    try:
        return liste.index(element, start)
    except ValueError:
        return -1
