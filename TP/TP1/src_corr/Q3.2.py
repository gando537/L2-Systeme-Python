import os, sys

def print_ids(mesg):
    """Print processus id and parent id"""
    print("%s: pid= %d, ppid= %d" % (mesg, os.getpid(), os.getppid()))

def produit_fils(f_fils):
    """Produit un processus fils et exécute ce fils"""
    pid = os.fork()
    if pid == 0:
        f_fils()

def sans_enfant(nom):
    """Retourne une fonction qui implémente un fils sans enfant"""
    def fonction():
        print_ids(nom)
        sys.exit(0)
    return fonction

def fils1():
    """Fonction qui implémente le fils1"""
    print_ids("fils1")
    produit_fils(sans_enfant("petit_fils1"))
    produit_fils(sans_enfant("petit_fils2"))
    sys.exit(0)

def pere():
    """Fonction qui implémente le père"""
    print_ids("père")
    produit_fils(fils1)
    produit_fils(sans_enfant("fils2"))
    produit_fils(sans_enfant("fils3"))

if __name__ == '__main__':
	pere()
