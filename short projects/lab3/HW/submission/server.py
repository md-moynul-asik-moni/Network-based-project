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
            hour = int(msg)
            if hour < 0:
                conn.send('hour can not be negative'.encode(FORMAT))
            else:
                if hour <= 40:
                    salary = 200*hour
                    conn.send(str(salary).encode(FORMAT))
                elif hour > 40:
                    salary = 8000 + ((hour-40)*300)
                    conn.send(str(salary).encode(FORMAT))

conn.close()