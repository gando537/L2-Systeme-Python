import os,sys

fd1 = os.open("toto.txt", os.O_RDONLY)
fd2 = os.open("toto.txt", os.O_RDONLY)

sbytes = os.read(fd1,2)
sbytes = os.read(fd2,1)
os.close(fd1)
os.close(fd2)
print("c = ", sbytes)
print("c = {}".format(sbytes.decode("utf-8")))
print("c = {}".format(sbytes.decode("latin-1")))
sys.exit(0)