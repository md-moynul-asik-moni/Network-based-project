import socket

HEADER = 16
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)



FORMAT = 'utf-8'
DISCONNECT_MSG = 'END'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


server.listen()
print('Server is listening....')
conn, addr = server.accept()
connected = True


while connected:
    msg_length = conn.recv(HEADER)
    if msg_length:
        msg_length = int(msg_length)
        msg = conn.recv(msg_length).decode(FORMAT)
        if msg == DISCONNECT_MSG:
            connected = False
            conn.send('Goodbye'.encode(FORMAT))
        else:
            vowels = 'aeiouAEIOU'
            count = 0
            for i in msg:
                if i in vowels:
                    count+=1
            if count == 0:
                conn.send('not enough vowels'.encode(FORMAT))
            elif count <= 2:
                conn.send('enough vowels ig'.encode(FORMAT))
            else:
                conn.send('too many vowels'.encode(FORMAT))

conn.close()