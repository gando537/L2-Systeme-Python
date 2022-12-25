import os, sys

def creation_famille(nf, npf):
    print("Père pid = %d" % os.getpid())
    for i in range(nf):
        p = os.fork()
        if p == 0: # Fils i
            print("Fils %d, pid = %d" % (i, os.getpid()))
            for j in range(npf):
                p = os.fork()
                if p == 0: # Petit-fils j
                    print("Petit-fils %d de %d, pid=%d"% (j, i, os.getpid()))
                    sys.exit(0)
                # Suite fils i
            sys.exit(0)
        # Suite père
    sys.exit(0)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('%s: Erreur, 2 arguments entiers attendus' % sys.argv[0], file=sys.stderr)
        sys.exit(2)
    ni, nj = map(int, sys.argv[1:3]) # on devrait vérifier le type avant le cast
    creation_famille(ni, nj)
