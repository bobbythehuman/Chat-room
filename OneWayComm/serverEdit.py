import time, socket, sys

new_socket = socket.socket()
host_name = socket.gethostname()
s_ip = socket.gethostbyname(host_name)
port = 8080
new_socket.bind((host_name, port))

print("This is a One Way Communication Server, you can only send messages.")
print("This is your IP: ", s_ip)
print("Your Port is ",port)

name = input('Enter name: ')

new_socket.listen(1)
conn, add = new_socket.accept()

# print("Received connection from ", add[0])
print('Connection Established. Connected From: ',add[0])

client = (conn.recv(1024)).decode()
print(client + ' has connected.')

conn.send(name.encode())
while True:
    message = input('Me : ')
    conn.send(message.encode()) # sends message
    #message = conn.recv(1024) # recieves messages
    #message = message.decode()
    #print(client, ':', message)