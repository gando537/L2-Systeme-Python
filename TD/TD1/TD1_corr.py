x = 1
pid = os.fork()
if pid == 0:
	x = x + 1
	print("child x = ", x)
	sys.exit(0)
x = x - 1
print("parent x = ", x)
sys.exit(0)

# Ce programme affiche : parent x = 0
#						 child x = 2


#---------------------------------Q2---------------------------------

os.fork()
os.fork()
os.fork()
print("hello !")
sys.exit(0)

# Ce programme affiche : hello ! huit fois

#---------------------------------Q3---------------------------------


for i in range(2):
	os.fork()
print("hello !")
sys.exit(0)

# Ce programme affiche : 4 hello !


def do_it():
	os.fork()
	os.fork()
	print("hello !")

if __name__ == '__main__':
	do_it()
	print("hello !")
	sys.exit(0)

# Ce programme affiche : 8 hello !

#---------------------------------Q4---------------------------------


parametre = int(sys.argv[1])
print(parametre)
print("pid = %d, ppid = %d" % (os.getpid(), os.getpid()))
for i in range(parametre):
	pid_fils = os.fork()
	if pid_fils == 0:
		print("pid = %d, ppid = %d" % (os.getpid(), os.getppid()))
	else :
		sys.exit(0)


parametre = int(sys.argv[1])
print(parametre)
print("pid = %d, ppid = %d" % (os.getpid(), os.getppid()))
for i in range(parametre):
	pid_fils = os.fork()
	if pid_fils == 0:
		print("pid = %d, ppid = %d" % (os.getpid(), os.getppid()))
		sys.exit(0)

#---------------------------------Q5.1---------------------------------


print(os.getpid())
pid1 = os.fork()
if pid1 == 0:
	print("fils = {} et père = {}".format(os.getpid(),os.getppid()))
	sys.exit(0)
else :
	pid = os.fork()
	if pid == 0:
		print("fils = {} et père = {}".format(os.getpid(),os.getppid()))
		sys.exit(0)


#---------------------------------Q5.2---------------------------------

print(os.getpid())
pid1 = os.fork()
if pid1 == 0:
	os.fork()
	print("fils = {} et père = {}".format(os.getpid(),os.getppid()))
sys.exit(0)

ou encore #--------------

print(os.getpid())
pid = os.fork()
if pid == 0:
	print("fils = {} et père = {}".format(os.getpid(),os.getppid()))
	petit_fils = os.fork()
	if petit_fils == 0:
		print("petit_fils = %d et père = %d" % (os.getpid(),os.getppid()))
		sys.exit(0) 

#---------------------------------Q5.3---------------------------------

while True:
	print(os.getpid())
	time.sleep(2)
	x = os.fork()
	if x != 0 :
		sys.exit(0)

#---------------------------------Q6.1---------------------------------


print(os.getpid())
for i in range(5):
	fils = os.fork()
	if fils == 0:
		print("fils %d = %d" % (i + 1, os.getpid()))
		sys.exit(0)

#---------------------------------Q6.2/3---------------------------------


parametre = int(sys.argv[1])
print(os.getpid())
for i in range(parametre):
	fils = os.fork()
	if fils == 0:
		print("fils %d = %d" % (i + 1, os.getpid()))
		sys.exit(0)

#---------------------------------Q7.1---------------------------------




























