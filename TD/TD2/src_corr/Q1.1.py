import os, sys

nbChildren = 20
lpid = []
for i in range(nbChildren):
    pid = os.fork()
    if pid == 0:  # child
        sys.exit(100 + i)
    else:
        lpid.append(pid)
# parent waits for all of its children to terminate
for p in lpid:
    pid, status = os.waitpid(p, 0)
    if os.WIFEXITED(status):
        print("child {} terminated normally with exit status={}".format\
                (pid, os.WEXITSTATUS(status)))
    else:
        print("child {} terminated abnormally".format(pid))
sys.exit(0)
