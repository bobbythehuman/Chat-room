import time, socket, sys
import random

def delitem(who, what):
    who.remove(what)
    
def createList(who, length):
    for x in range(length):
        who.append(random.randrange(1,10))

def userinput(who):
    temp=-1
    while temp not in who:
        print(who)
        temp=int(input("choose a number from the list above: "))
    delitem(who,temp)
    return temp

two=[]
t=0
end=False
message=""

socket_server = socket.socket()
server_host = socket.gethostname()
ip = socket.gethostbyname(server_host)
sport = 8080
print("The aim of the game is to choose a number from the list that is higher than your opponent's number.")
print('This is your IP address: ',ip)
server_host = input('Enter friend\'s IP address: ')
name = input('Enter your name: ')


createList(two,5)


socket_server.connect((server_host, sport))
socket_server.send(name.encode())
server_name = (socket_server.recv(1024)).decode()
print(server_name,' has joined...')

while len(two)>0:
    t=str(userinput(two))
    socket_server.send(t.encode())
    message = (socket_server.recv(1024)).decode() #recieves message
    print(message)
    #message = (socket_server.recv(1024)).decode() #recieves message

message = (socket_server.recv(1024)).decode() #recieves message
print(message)

end=input("enter to close")