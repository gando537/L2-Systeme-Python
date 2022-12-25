import os, sys

def print_ids(mesg):
    """Print processus id and parent id"""
    print("%s: pid=%d, ppid=%d" % (mesg, os.getpid(), os.getppid()))

# Au début, était le père...
print_ids("pere")
if os.fork() == 0:
    # puis vint le fils1 ...
    print_ids("fils1")
    # le fils1 eut lui même des fils
    if os.fork() == 0:
        # petit-fils 1
        print_ids("petit-fils1")
        sys.exit(0) # pf1 a fini
    # Seul fils 1 continue ici. Il peut faire un deuxième fils
    if os.fork() == 0:
        # petit-fils 2
        print_ids("petit-fils2")
        sys.exit(0) # pf2 a fini
    # Seul fils 1 continue ici. Il a terminé.
    os.wait()
    os.wait()
    sys.exit(0) # f1 a fini
# seul le père continue ici. Il peut faire un 2e fils
os.wait()
if os.fork() == 0:
    print_ids("fils2")
    # Le fils 2 n’a pas de fils, il peut se terminer.
    sys.exit(0) # f2 a fini
# seul le père continue ici. Il peut faire un 3e fils
if os.fork() == 0:
    print_ids("fils3")
    # Le fils 3 n’a pas de fils, il peut se terminer.
    sys.exit(0) # f3 a fini
# seul le père continue ici. Il a terminé
