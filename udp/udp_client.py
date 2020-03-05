import socket
import random

UDP_IP = '127.0.0.1'
UDP_PORT = 4000
BUFFER_SIZE = 1024
FILE_TO_UPLOAD = "upload.txt"


def send(id=0):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        with open(FILE_TO_UPLOAD) as file:
            for line in file:
                #Resend every packet 5 times if SEQUENCE numbers not matches
                for i in range(6):
                    SEQ_NO = random.sample(range(1, 10000), 1)
                    print(f'Sequence number sent:{SEQ_NO}')
                    message = str(SEQ_NO)+":"+line
                    s.sendto(f"{id}:{message}".encode(), (UDP_IP, UDP_PORT))
                    data, ip = s.recvfrom(BUFFER_SIZE)
                    data = data.decode(encoding="utf-8").strip()
                    SEQ_RECVD = data[:]
                    #SEQ_RECVD=[000]
                    print(f'Sequence number received from server:{SEQ_RECVD}')
                    #Resend message if send and recived SEQUENCE no not matches
                    if str(SEQ_NO) == str(SEQ_RECVD):
                        print("SEQUENCE NO matched")
                        break;

                else:
                    print("Acknowledgment not received from server after multiple trials, not sending other packets")
                    break;



    except socket.error:
        print("Error! {}".format(socket.error))
        exit()



def get_client_id():
    id = input("Enter client id:")
    return id

send(get_client_id())
