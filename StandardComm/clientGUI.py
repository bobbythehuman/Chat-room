import socket
from threading import Thread

class MSGLimit():
    def __init__(self,name):
        self.msg = ""
        self.allMSG = []
        self.name = name
    def display(self,size):
        self.msg=""
        for x in self.allMSG[-size:]:
            self.msg = self.msg+x+"\n"
        return self.msg
    def newMSG(self,msg):
        self.allMSG.append(msg)
print(socket.gethostname())
print(f"Current ip {socket.gethostbyname(socket.gethostname())}")
SERVER_HOST = input("Enter ip: ")
SERVER_PORT = 5002
separator_token = "<SEP>"

s = socket.socket()
print(f"[*] Connecting to {SERVER_HOST}:{SERVER_PORT}...")
s.connect((SERVER_HOST, SERVER_PORT))
print("[+] Connected.")

name = input("Enter your name: ")



sm = MSGLimit("sentMSG")
rm = MSGLimit("receivedMSG")

from PyQt6 import QtWidgets, QtCore
import sys

class ChatWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Window Title')
        self.resize(620, 498)

        main_layout = QtWidgets.QVBoxLayout(self)

        top_layout = QtWidgets.QHBoxLayout()

        self.received = QtWidgets.QTextEdit()
        self.received.setReadOnly(True)
        self.received.setStyleSheet('background-color: red;')
        self.received.setPlaceholderText('Received')

        self.sent = QtWidgets.QTextEdit()
        self.sent.setReadOnly(True)
        self.sent.setStyleSheet('background-color: green;')
        self.sent.setPlaceholderText('Sent')

        top_layout.addWidget(self.received)
        top_layout.addWidget(self.sent)

        main_layout.addLayout(top_layout)

        bottom_layout = QtWidgets.QHBoxLayout()
        self.msg_input = QtWidgets.QLineEdit()
        self.msg_input.setPlaceholderText('Input')
        self.send_btn = QtWidgets.QPushButton('Send')
        self.send_btn.clicked.connect(self.on_send)

        bottom_layout.addWidget(self.msg_input)
        bottom_layout.addWidget(self.send_btn)

        main_layout.addLayout(bottom_layout)

        # Timer to refresh displays (safe from non-GUI thread)
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_displays)
        self.timer.start(200)  # ms

    def closeEvent(self, event):
        try:
            s.close()
        except Exception:
            pass
        event.accept()

    def on_send(self):
        to_send = self.msg_input.text()
        if to_send == '':
            return
        sm.newMSG(to_send)
        self.update_sent()
        payload = f"{name}{separator_token}{to_send}"
        try:
            s.send(payload.encode())
        except Exception as e:
            print('Send failed:', e)
        self.msg_input.clear()

    def update_received(self):
        fm = self.received.fontMetrics()
        line_h = max(1, fm.lineSpacing())
        rows = max(1, int(self.received.height() / line_h))
        self.received.setPlainText(rm.display(rows))

    def update_sent(self):
        fm = self.sent.fontMetrics()
        line_h = max(1, fm.lineSpacing())
        rows = max(1, int(self.sent.height() / line_h))
        self.sent.setPlainText(sm.display(rows))

    def update_displays(self):
        self.update_received()
        self.update_sent()


def listen_for_messages():
    while True:
        try:
            message = s.recv(1024).decode()
            if not message:
                print('Server closed connection.')
                break
            rm.newMSG(message)
        except Exception as e:
            print('Receive error:', e)
            break



t = Thread(target=listen_for_messages)
t.daemon = True
t.start()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = ChatWindow()
    win.show()
    ret = app.exec()
    try:
        s.close()
    except Exception:
        pass
    sys.exit(ret)