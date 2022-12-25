
import os,sys

fd1 = os.open("toto.txt", os.O_RDONLY)
fd2 = os.open("toto.txt", os.O_RDONLY)
c = os.read(fd2, 1)
os.dup2(fd2, fd1)
c = os.read(fd1, 1)
print("c = {}".format(c))
sys.exit(0)