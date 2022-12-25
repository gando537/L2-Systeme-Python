import os, sys

if len(sys.argv) < 2:
	print("Wrong number of arguments. At least 1 arg exected", file=sys.stderr)
	sys.exit(1)

cmd = sys.argv[1]
args = sys.argv[1:] # we have to pass the name of the program as it's first arg
print(cmd)
print(args)

# os.execv() does not use the PATH (it does not look into env variables
# but passes them along to the new process)
# os.execvp() does use the PATH
# os.execve() and os.exevcpe() allows to pass a modified environment to the process 
# os.execvpe() uses the modified PATH
os.execvp(cmd, args)
