import os, signal, sys
from utils import execvp_with_exception_handling, indice

def usage(cmd):
    print("%s: usage: %s com1 ... --then com2 ... [ --else com3 ... ] --fi" % (cmd, cmd), \
            file=sys.stderr)

if __name__ == '__main__':
    index_then = indice(sys.argv, '--then', 2)
    index_else = indice(sys.argv, '--else', index_then + 2)
    index_fi = indice(sys.argv, '--fi', max(index_then, index_else) + 2)
    if index_then == -1 or index_fi != len(sys.argv) - 1:
        usage(sys.argv[0])
        sys.exit(1)
    # On va exécuter com1
    if os.fork() == 0: # Fils
        execvp_with_exception_handling(sys.argv[1], sys.argv[1:index_then])    
    # Suite père
    pid, status = os.wait()
    if os.WIFEXITED(status) and os.WEXITSTATUS(status) == 0: # success 
        a = index_then + 1
        b = index_else
    elif os.WIFSIGNALED(status) or os.WIFEXITED(status): # killed by signal or failure (WIFSTOPPED can happen)
        if index_else == -1:
            sys.exit(0)
        a = index_else + 1
        b = index_fi
    os.execvp(sys.argv[a], sys.argv[a:b])
