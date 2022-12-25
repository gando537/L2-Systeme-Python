import os, sys

def print_ids(mesg):
    """Print processus id and parent id"""
    print("%s: pid= %d, ppid= %d" % (mesg, os.getpid(), os.getppid()))

# Au début, était le père...
print_ids("père")
pid1 = os.fork()
if pid1 == 0:
    # puis vint le fils1 ...
    print_ids("fils1")
    # le fils1 eut lui même des fils
    pid1_1 = os.fork()
    if pid1_1 == 0:
        # petit-fils 1
        print_ids("petit-fils1")
        sys.exit(0) # pf1 a fini
    # Seul fils 1 continue ici. Il peut faire un deuxième fils
    pid1_2 = os.fork()
    if pid1_2 == 0:
        # petit-fils 2
        print_ids("petit-fils2")
        sys.exit(0) # pf2 a fini
    # Seul fils 1 continue ici. Il a terminé.
    sys.exit(0) # f1 a fini
# seul le père continue ici. Il peut faire un 2e fils
pid2 = os.fork()
if pid2 == 0:
    print_ids("fils2")
    # Le fils 2 n'a pas de fils, il peut se terminer.
    sys.exit(0) # f2 a fini
# seul le père continue ici. Il peut faire un 3e fils
pid3 = os.fork()
if pid3 == 0:
    print_ids("fils3")
    # Le fils 3 n'a pas de fils, il peut se terminer.
    sys.exit(0) # f3 a fini
# seul le père continue ici. Il a terminé
