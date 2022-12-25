import os

#for k in sorted(os.environ):
#    print(k + "= " + os.environ[k])

os.environ['USER'] = 'roland'

pid1 = os.fork()
if pid1 == 0: #child
    print(os.environ['USER'])
    
