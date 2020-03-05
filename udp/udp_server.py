import socket


UDP_IP = '127.0.0.1'
UDP_PORT = 4000
BUFFER_SIZE = 1024
MESSAGE = "pong"

def listen_forever():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("", UDP_PORT))
    print(f'Server started at port {UDP_PORT}')

    while True:
        # get the data sent to us
        data, ip = s.recvfrom(BUFFER_SIZE)
        print("{}: {}".format(ip, data.decode(encoding="utf-8").strip()))
        data = data.decode(encoding="utf-8").strip()
        client, SEQ_NO, ID, message = data.split(':',-1)
        print(f'Sequence number received: {SEQ_NO}')
        # reply back received sequence to the client
        s.sendto(SEQ_NO.encode(), ip)


listen_forever()