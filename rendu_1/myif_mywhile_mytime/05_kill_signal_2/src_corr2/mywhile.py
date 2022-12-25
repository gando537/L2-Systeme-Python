import os, signal, sys
from utils import execvp_with_exception_handling, indice

def SIGINT_handler(sig, ign):
    sys.exit(130)

def usage(cmd):
    print("%s: usage: %s com1 ... --do com2 ... --done" % (cmd, cmd), \
            file=sys.stderr)

if __name__ == '__main__':
    signal.signal(signal.SIGINT, SIGINT_handler)
    ind_do   = indice(sys.argv, "--do", 2)
    ind_done = indice(sys.argv, "--done", ind_do + 2)
    if ind_do == -1 or ind_done != len(sys.argv) - 1:
        usage(sys.argv[0])
        sys.exit(1)
    status_com2 = 0
    while True:
        # On va exécuter com1
        if os.fork() == 0: # Fils 1
            execvp_with_exception_handling(sys.argv[1], sys.argv[1:ind_do])
        # Suite père
        pid, status_com1 = os.wait() # attente résultat com1
        if os.WIFSIGNALED(status_com1):
            if os.WTERMSIG(status_com1) == signal.SIGINT:
                sys.exit(130)
            else:
                sys.exit(0)
        elif os.WIFEXITED(status_com1):
            if os.WEXITSTATUS(status_com1) != 0:
                sys.exit(status_com2)
            # On va exécuter com2
            if os.fork() == 0:  # Fils 2
                os.execvp(sys.argv[ind_do+1], sys.argv[ind_do+1:ind_done])          
            # Suite père
            pid, status_com2 = os.wait()
