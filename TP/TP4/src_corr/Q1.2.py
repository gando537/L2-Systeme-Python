import os, sys

MAXBYTES = 1000

def child1():
    os.close(rfd1)
    buff = os.read(0, MAXBYTES)
    while len(buff) > 0:
       os.write(wfd1, buff)  # écrire contenu de l'entrée standard sur le tube
       buff = os.read(0, MAXBYTES)
    print('fils 1 a terminé')
    os.close(wfd1) # the other end of the pipe will see CTRL-D
				   # if father's wfd1 is also closed

def child2():
    os.close(wfd1)
    buff = os.read(rfd1, MAXBYTES)
    while len(buff) > 0:
       os.write(1, buff)  # écrire contenu du tube sur la sortie standard
       buff = os.read(rfd1, MAXBYTES)
    print('fils 2 a terminé')

if __name__ == '__main__':
	rfd1, wfd1 = os.pipe()
	childpid1 = os.fork()
	if childpid1 == 0:
		child1()
		sys.exit(0)
	childpid2 = os.fork()
	if childpid2 == 0:
		child2()
		sys.exit(0)

	os.close(rfd1)
	os.close(wfd1) # mandatory : as long as the father has it opened, 
				   # child2 can't see CTRL-D
	os.waitpid(childpid2, 0)
	print('père se termine')
