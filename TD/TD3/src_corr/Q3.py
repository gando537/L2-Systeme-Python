import os, sys

if __name__ == '__main__':
    commandes = [('who', ['who']), ('pwd', ['pwd']), ('ls', ['ls', '-l'])]
    print("Père pid = %d" % os.getpid())
    for i in range(3):
        p = os.fork()
        if p == 0: # Fils i
            print("Fils %d, pid = %d" % (i, os.getpid()))
            commande, args = commandes[i]
            os.execvp(commande, args)
        # Suite père
        print("Père: attente fin fils %d" % i)
        os.wait() # or os.waitpid(p, 0)
        print("Père : fin fils %d détectée" % i)
    sys.exit(0)

