import errno, os, sys, time

N_wait = 5
for i in range(N_wait):
    pid = os.fork()
    if pid == 0:  # child
        time.sleep(5)
        sys.exit(100 + i)
    else: # parent
        print(str(pid) + " créé")
try:
    # parent waits for all of its children to terminate
    pid, status = os.waitpid(-1, 0)
    while True:
        if os.WIFEXITED(status):  
            print("child %d terminated normally with exit status=%d" %\
                (pid, os.WEXITSTATUS(status)))
        else:
            print("child %d terminated abnormally" % pid)
            if os.WIFSIGNALED(status) :
                print("il a été tué par le signal non traité {}".\
                    format(os.WTERMSIG(status)))
        pid, status = os.waitpid(-1, 0)
except OSError as err:
    #print ("{}".format(err))
    if err.errno != errno.ECHILD:
        print("waitpid error(%d): %s" % (err, strerror(err.errno)))
sys.exit(0)
