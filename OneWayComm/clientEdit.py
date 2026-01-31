import time, socket, sys

socket_server = socket.socket()
server_host = socket.gethostname()
ip = socket.gethostbyname(server_host)
sport = 8080

print('Welcome to One Way Communication, you can only receive messages.')
print('This is your IP address: ',ip)
server_host = input('Enter friend\'s IP address: ')
name = input('Enter your name: ')

socket_server.connect((server_host, sport))
socket_server.send(name.encode())
server_name = socket_server.recv(1024)
server_name = server_name.decode()

print(server_name,' has joined...')
while True:
    message = (socket_server.recv(1024)).decode() #recieves message
    print(server_name, ":", message)
    #message = ("True")
    #socket_server.send(message.encode()) #sends messages