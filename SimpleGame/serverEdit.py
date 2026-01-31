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

one=[]
oneW=0
o=0

two=[]
twoW=0
t=0

createList(one,5)
print("The aim of the game is to choose a number from the list that is higher than your opponent's number.")

new_socket = socket.socket()

host_name = socket.gethostname()
s_ip = socket.gethostbyname(host_name)

port = 8080
new_socket.bind((host_name, port))
print("Binding successful")
print("This is your IP: ", s_ip)
print("Your Port is ",port)
name = input('Enter name: ')

new_socket.listen(1)
conn, add = new_socket.accept()
print("Received connection from ", add[0])
print('Connection Established. Connected From: ',add[0])

client = (conn.recv(1024)).decode()
print(client + ' has connected.')
conn.send(name.encode())

while len(one)>0:
    o=userinput(one)
    t=int((conn.recv(1024)).decode())
    if o>t:
        message=f"{name} wins"
        print(message)
        conn.send(message.encode())
        oneW=oneW+1
    elif t>o:
        message=f"{client} wins"
        print(message)
        conn.send(message.encode())
        twoW=twoW+1
    else:
        message="Draw"
        print(message)
        conn.send(message.encode())
#conn.send("end".encode())

if oneW>twoW:
    message=f"{name} wins the match"
    print(message)
    conn.send(message.encode())
elif twoW>oneW:
    message=f"{client} wins the match"
    print(message)
    conn.send(message.encode())
else:
    message="the match was drawn"
    print(message)
    conn.send(message.encode())

end=input("enter to close")