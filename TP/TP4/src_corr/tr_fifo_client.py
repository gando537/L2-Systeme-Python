import os, sys
import tr_client_server

wfd1 = os.open("/tmp/ma_fifo1", os.O_WRONLY) # ouvre fifo1 en ecriture
rfd2 = os.open("/tmp/ma_fifo2", os.O_RDONLY) # ouvre fifo2 en lecture
tr_client_server.client(rfd2, wfd1)          # pere execute client
os.close(wfd1)
sys.exit(0)
