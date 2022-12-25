import os

os.environ['PATH'] = 'Rien du tout dans le Path'
os.execve('/usr/bin/python3', ['python3', 'afficheur.py'], os.environ)
