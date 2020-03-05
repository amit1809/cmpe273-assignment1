import socket
import random

UDP_IP = '127.0.0.1'
UDP_PORT = 4000
BUFFER_SIZE = 1024
#MESSAGE = "1,2,3,4,5"
FILE_TO_UPLOAD = "upload.txt"


def send(id=0):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        upload_file(s)

    except socket.error:
        print("Error! {}".format(socket.error))
        exit()

def upload_file(s):
    with open(FILE_TO_UPLOAD) as file:
        for line in file:
            line = line.strip()
            # print(line)
            # sequence, message = line.split(":")
            # print(sequence)
            # print(message)
            SEQ_NO = random.sample(range(1, 10000), 1)
            print(SEQ_NO)
            s.sendto(f"{id}:{line}".encode(), (UDP_IP, UDP_PORT))
            data, ip = s.recvfrom(BUFFER_SIZE)
            print("received data: {}: {}".format(ip, data.decode()))



def get_client_id():
    id = input("Enter client id:")
    return id

send(get_client_id())

'''
        s.sendto(f"{id}:{MESSAGE}".encode(), (UDP_IP, UDP_PORT))
        data, ip = s.recvfrom(BUFFER_SIZE)
        print("received data: {}: {}".format(ip, data.decode()))
    except socket.error:
        print("Error! {}".format(socket.error))
        exit()

'''