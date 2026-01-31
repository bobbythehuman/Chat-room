import socket
from threading import Thread

SERVER_HOST = socket.gethostbyname(socket.gethostname())
SERVER_PORT = 5002
separator_token = "<SEP>"
print(SERVER_HOST,SERVER_PORT)
client_sockets = set()
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((SERVER_HOST, SERVER_PORT))
s.listen(5)
print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")

def listen_for_client(cs):
    while True:
        try:
            msg = cs.recv(1024).decode()
        except Exception as e:
            try:
                client_sockets.remove(cs)
            except:
                print(f"[!] Error: {e}")
                exit()
            finally:
                msg = f"[!] A client has disconnected."
        else:
            msg = msg.replace(separator_token, ": ")
            print(msg)
        for client_socket in client_sockets:
            client_socket.send(msg.encode())

while True:
    client_socket, client_address = s.accept()
    print(f"[+] {client_address} connected.")
    client_sockets.add(client_socket)
    t = Thread(target=listen_for_client, args=(client_socket,))
    t.daemon = True
    t.start()

print("here")
for cs in client_sockets:
    cs.close()
s.close()
exit()