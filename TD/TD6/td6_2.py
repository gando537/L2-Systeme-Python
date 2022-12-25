import os,sys

fd1 = os.open("toto.txt", os.O_RDONLY)

sbytes = os.read(fd1,2)
print("c = ", sbytes)
print("c = {}".format(sbytes.decode("utf-8")))
sbytes = os.read(fd1,1)
print("c = ", sbytes)
print("c = {}".format(sbytes.decode("utf-8")))
sys.exit(0)