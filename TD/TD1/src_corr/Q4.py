# Rappel: tout ce qui suit un # est un commentaire
import os, sys

# Récupère le premier paramètre de la ligne de commande
n = int(sys.argv[1])

# Comme sur le dessin, le père commence toujours par afficher
print("pid={}, ppid={}".format(os.getpid(), os.getppid()))
# La chaine de gauche
for i in range(n):
    pid_fils = os.fork()
    if pid_fils == 0:
        # si la variable pid_fils vaut zero, c'est qu'on est le fils
        # Or d'après le dessin, le fils doit afficher puis continuer 
        print("pid={}, ppid={}".format(os.getpid(), os.getppid()))
    else:
        # Seul le père passe ici: il meurt sans rien afficher
        sys.exit(0)

# Comme sur le dessin, le père commence toujours par afficher
print("pid={}, ppid={}".format(os.getpid(), os.getppid()))
for i in range(n):
    pid_fils = os.fork()
    if pid_fils == 0:
        # si la variable pid_fils vaut zero, c'est qu'on est le fils
        # Or d'après le dessin, le fils doit mourir après affichage
        print("pid={}, ppid={}".format(os.getpid(), os.getppid()))
        sys.exit(0)
    # Seul le père passe ici, puisque le fils meurt dans le if
    # Le père n'affiche rien
