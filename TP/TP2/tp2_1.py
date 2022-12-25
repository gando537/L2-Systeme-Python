import os, sys, time , signal, errno

def sleep():
	parametre = float(sys.argv[1])
	time.sleep(parametre)

sleep()