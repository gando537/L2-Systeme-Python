import atexit, os, sys
import tr_client_server

def _clean():
    #print("clean-up", file=sys.stderr)
    try:
        os.unlink("/tmp/ma_fifo1")         # faire le ménage sur disque....
        os.unlink("/tmp/ma_fifo2")  
    except FileNotFoundError:
        pass

if __name__ == '__main__':
    atexit.register(_clean)
    if len(sys.argv) < 3:
        print(sys.argv[0], "entree sortie", file=sys.stderr)
        sys.exit(1)
    e, s = sys.argv[1], sys.argv[2]
    os.mkfifo("/tmp/ma_fifo1")
    os.mkfifo("/tmp/ma_fifo2")
    rfd1 = os.open("/tmp/ma_fifo1", os.O_RDONLY) # ouvre fifo1 en lecture
    wfd2 = os.open("/tmp/ma_fifo2", os.O_WRONLY) # ouvre fifo2 en écriture
    tr_client_server.server(rfd1, wfd2, e, s)
    os.close(wfd2)
    sys.exit(0)
