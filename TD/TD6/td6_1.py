import os,sys

fd1 = os.open("toto.txt", os.O_RDONLY)
print("fd1 = {}".format(fd1))
os.close(fd1)
fd2 = os.open("titi.txt", os.O_RDONLY)
print("fd2 = {}".format(fd2))
fd3 = os.open("titi.txt", os.O_RDONLY)
print("fd3 = {}".format(fd3))

os.close(fd2)
os.close(fd3)

sys.exit(0)