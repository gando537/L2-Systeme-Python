import os, sys
# programme générique client-serveur

# Les deux modules suivants doivent être écrit
# ils sont supposés fournir les deux méthodes
# client.client() et server.server()
import client, server 

if __name__ == "__main__":
   os.mkfifo("/tmp/ma_fifo1")
   os.mkfifo("/tmp/ma_fifo2")
   childpid = os.fork()
   if childpid == 0:
       rfd1 = os.open("/tmp/ma_fifo1", os.O_RDONLY) # ouvre fifo1 en lecture
       wfd2 = os.open("/tmp/ma_fifo2", os.O_WRONLY) # ouvre fifo2 en ecriture
       server.server(rfd1, wfd2)      # fils exécute serveur
       sys.exit(0)
   wfd1 = os.open("/tmp/ma_fifo1", os.O_WRONLY) # ouvre fifo1 en écriture
   rfd2 = os.open("/tmp/ma_fifo2", os.O_RDONLY) # ouvre fifo2 en lecture
   client.client(rfd2, wfd1)          # père exécute client
   os.waitpid(childpid, 0)            # attendre fin fils
   os.unlink("/tmp/ma_fifo1")         # faire le ménage sur disque....
   os.unlink("/tmp/ma_fifo2")
   sys.exit(0)
