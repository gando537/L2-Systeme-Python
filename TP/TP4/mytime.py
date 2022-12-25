import os, signal, sys, time

def indice(liste, element, start):
    try:
        return liste.index(element, start)
    except ValueError:
        return -1

def afficher_usage():
    print("Usage: %s [-n k] [-s] [--no-outpout] commande [arg ...]", sys.argv[0], file=sys.stderr)
    sys.exit(1)

if __name__ == '__main__':
    
    op_n = op_s = op_no_outpout= False
    k = 1
    ind_commande = 1
    
    ind_n = indice(sys.argv, '-n', 1)
    ind_s = indice(sys.argv, '-s', 1)
    ind_no_outpout = indice(sys.argv, '--no-outpout', 1)
    
    if ind_n > -1:
        ind_commande += 2
        op_n = True
        k = int(sys.argv[ind_n + 1])
        if k < 0:
            afficher_usage()
    if ind_s > -1:
        ind_commande += 1
        op_s = True
    
    if len(sys.argv) <= ind_commande:
        afficher_usage()

    if ind_no_outpout > -1:

        sov_stdout = os.dup(1)
        sov_stderr = os.dup(2)

        ind_commande += 1
        op_no_outpout = True
        fd = open(os.devnull, 'w')
        sys.stdout = fd
        sys.stderr = fd
        os.dup(sys.stdout)
        os.dup(sys.stderr)

    durk = 0
    for i in range(k):
        n = os.fork()
        if n == 0: 
            try:
                os.execvp(sys.argv[ind_commande], sys.argv[ind_commande:])
            except FileNotFoundError:
                sys.exit (1)
        
        t1 = time.time()
        pid, status = os.wait()
        t2 = time.time()
        dur1 = t2 - t1
        durk += dur1
        if k > 1:
            print("Itération %d - " % i, end='')
        print("Durée %.6lf s" % dur1, end='')
        if (op_s):
            print(" - Code de sortie : %d" % os.WEXITSTATUS(status), end='')
        print()
    if k > 1: 
        print("Durée Moyenne : %.6f s" % (durk / k))
    sys.exit(0)


