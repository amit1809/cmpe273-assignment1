import socket
import threading

TCP_IP = '127.0.0.1'
TCP_PORT = 5000
BUFFER_SIZE = 1024
conns_list = []
addr_list = []


def listen_forever():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(1)
    print(f'Server started at port {TCP_PORT}')
    while True:
        conn, addr = s.accept()
        print(f'Connected Client:{addr}')
        #print(conn)
        s.setblocking(1)  # to prevent timeout
        conns_list.append(conn)
        addr_list.append(addr)


def data_receive_send():
    while True:
        for i, conn in enumerate(conns_list):
            data = conn.recv(BUFFER_SIZE)
            if not data:
                # print('No data received.')
                del conns_list[i]
                del addr_list[i]
                break
            print(f"Received data:{data.decode()}")
            conn.send("pong".encode())
            #del conns_list[i]
            #del addr_list[i]

    # conn.close()

listen_thread = threading.Thread(target=listen_forever)
#listen_thread.daemon = True
data_thread = threading.Thread(target=data_receive_send)
#data_thread.daemon = True


listen_thread.start()
data_thread.start()
