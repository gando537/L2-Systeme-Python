import os, socket, sys, errno,select, signal

def my_hand(sig,_):
    print("\nConnection closed...")
    sys.exit()

signal.signal(signal.SIGINT,my_hand)

if len(sys.argv) != 3:
    print('Usage:', sys.argv[0], 'hote port')
    sys.exit(1)

HOST = sys.argv[1]
PORT = int(sys.argv[2])
MAXBYTES = 10000

print("""
    \t -----------------------------------------------------------------------
    \t|\t              BIENVENUE !!!                                     |
    \t|\tQuelques commandes de bases :                                   |
    \t|\t- saisir pseudonyme ex: gan2                                    |
    \t|\t- Pour écrire à tout le monde : écrire et taper Entrée          |
    \t|\t- Pour écrire à une personne : écrire son pseudo en le précédent|
    \t|\t  de _@ ex: _@gan2 ensuite le message puis Entrée pour envoyer  |
    \t|\t- Pour connaître la liste des connectés, écrire : _@liste       |
    \t|\t- Pour se déconnecter : CTRL-D au clavier                       |
    \t|\t- D'abord veuillez saisir votre pseudo...                       |
    \t -----------------------------------------------------------------------
    """)

my_username=''
while my_username=='':
    my_username = input("Username : ")

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockaddr = (HOST, PORT)
conn = client_socket.connect(sockaddr)
client_socket.setblocking(False)
print('@{} is connected to: {}'.format(my_username, sockaddr))
username = my_username.encode('utf-8')
username_header = f"{len(username):<{MAXBYTES}}".encode('utf-8')
client_socket.send(username_header + username)

utlisatr = username.decode('utf-8')
while True:

    cur = f"@{utlisatr} > "
    print(cur,end='',flush=True)
    list_socket = [client_socket,0]
    activesocket, _,_ = select.select(list_socket,[],[])
    for s in activesocket:

        if s == 0:
            line = os.read(0,MAXBYTES)
            if len(line) == 0:
                client_socket.shutdown(socket.SHUT_WR)
                print("\nConnection closed...")
                sys.exit()

            mess = line.decode('utf-8')
            message = mess[:-1]

            if message != '\n':
                message = message.encode('utf-8')
                message_header = f"{len(message):<{MAXBYTES}}".encode('utf-8')
                client_socket.send(message_header + message)

        try:
            while True:
                username_header = client_socket.recv(MAXBYTES)
                user_nam = username_header.decode('utf-8')

                liste_use = user_nam.split()

                usenm = liste_use[-1]
                if user_nam.startswith('@server > _@kick'):
                    
                    if usenm == utlisatr:
                        print("\nConnection closed by server")
                        sys.exit()
                    else:
                        print('\n{} is deconnected...'.format(usenm))
                elif user_nam.startswith('@server >'):
                    mess_serv = '\n' + user_nam + '\n'
                    mess_rec = mess_serv.encode('utf-8')
                    os.write(1,mess_rec)
                else:
                    username_length = int(user_nam.strip())
                    username = client_socket.recv(username_length).decode('utf-8')

                    message_header = client_socket.recv(MAXBYTES)
                    message_length = int(message_header.decode('utf-8').strip())
                    message = client_socket.recv(MAXBYTES).decode('utf-8') + '\n'
                    mess_aff = f"\n@{username} > {message}".encode('utf-8')

                    os.write(1,mess_aff)

        except IOError as e:
            if e.errno != errno.EAGAIN and e.errno != EWOULDBLOCK:
                print("Reading error", str(e))
                sys.exit()
            continue

        except Exception as e:
            print("\nConnection closed by server")
            sys.exit()

client_socket.close()

