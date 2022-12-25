import os, sys, time , signal, errno

def time_sleep():
	parametre = float(sys.argv[1])
	time.sleep(parametre)
	sys.exit(0)

time_sleep()