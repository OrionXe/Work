import socket
import threading

HEADER = 64  # the lenght of msg rcv
PORT = 5050
# SERVER="192.168.0.100"
SERVER = socket.gethostbyname(socket.gethostname())  # automatically find the IPv4 adress
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"  # when we receive this msg we disconnect the server
print(socket.gethostname())

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # family, type
server.bind(ADDR)  # it binds the socket to the specific adress ADDR that includes the server and the port

def handle_client(conn, addr):  # it handles the message for each client individually
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:  #if the message is sent
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}] {msg}")
            conn.send("Msg received".encode(FORMAT))

    conn.close()

def start():
    server.listen()
    print(f"[LISTENING] server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))  # tells the thread 'location'
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount()-1}")

print("[STARTING]server is starting...")
start()

