import os, sys
import tr_client_server

if len(sys.argv) < 3:
    print(sys.argv[0], "entree sortie", file=sys.stderr)
    sys.exit(1)
e, s = sys.argv[1], sys.argv[2]
rfd1, wfd1 = os.pipe()                   # tube père vers fils
rfd2, wfd2 = os.pipe()                   # tube fils vers père
childpid = os.fork()
if childpid == 0: # child
     os.close(rfd1)
     os.close(wfd2)
     tr_client_server.client(rfd2, wfd1) # fils exécute client
else:             # father
     os.close(wfd1)
     os.close(rfd2)
     tr_client_server.server(rfd1, wfd2, e, s) # père éxecute serveur
     os.waitpid(childpid, 0)                   # attendre fin fils
sys.exit(0)
