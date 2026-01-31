# Chat-room
A collection of chat room using a server and clients
## Standard Chat Room
A simple chat room where multiple clients can connect to a server and exchange messages in real-time.
### How to Run
1. Navigate to the `StandardComm` directory:
2. Start the server
3. Start either `client.py` or `clientgui.py` then provide the server IP to connect.
4. To send messages:
    - For `client.py`, type the message in the client console
    - For `clientgui.py`, type the message in the GUI input box and press 'Send'

## One Way Chat Room
A chat room where messages can only be sent from the server to the clients.
### How to Run
1. Navigate to the `OneWayComm` directory
2. Start the server `serverEdit.py`
3. Start `clientEdit.py` then provide the server IP
4. Type messages in the server console to send them to all connected clients

## Simple Game Chat Room
A simple game using the same communication method as the standard chat room.
### How to Run
1. Navigate to the `SimpleGame` directory
2. Start the server `serverGame.py`
3. Start `clientGame.py` then provide the server IP
4. Both the server and client will receive a list of numbers
5. Type a number from the list and who ever types the highest number wins that round
6. Who ever wins the most rounds wins the game
7. To restart the game, restart both the server and client