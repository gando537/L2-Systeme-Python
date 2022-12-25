#! /usr/bin/env python
# file: server.py (module server)
import sys,os

def server(readfd, writefd):
    global MAXLINE
    buff = os.read(readfd, MAXLINE) 
    try:
    	fd = os.open(buff, os.O_RDONLY) 
    except:
    	os.write(writefd,buff) 
    	sys.exit(1)
    buff = os.read(fd, MAXLINE)
    while (buff.len > 0):
    	os.write(writefd,buff)
    	buff = os.read(fd, MAXLINE)
    os.close(fd)