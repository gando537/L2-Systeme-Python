#! /usr/bin/env python

import os,sys

fd1 = os.open("toto.txt", os.O_RDONLY) 
fd2 = os.open("toto.txt", os.O_RDONLY) 
c = os.read(fd1, 1)
c = os.read(fd2, 10)
print("c = {}".format(c)) 
sys.exit(0)