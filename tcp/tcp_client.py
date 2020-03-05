import socket
import time


TCP_IP = '127.0.0.1'
TCP_PORT = 5000
BUFFER_SIZE = 1024
MESSAGE = "ping"

def send(id=0, delay =0 , number_of_pings =1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    for i in range(number_of_pings):
        print("Sending data:", MESSAGE)
        s.send(f"{id}:{MESSAGE}".encode())
        data = s.recv(BUFFER_SIZE)
        # s.close()
        print("received data:", data.decode())
        time.sleep(delay)
'''
    data = s.recv(BUFFER_SIZE)
    #s.close()
    print("received data:", data.decode())
'''

def get_client_id():
    id = input("Enter client id:")
    return id

def get_delay():
    delay = input("Enter delay in seconds between messages:")
    return int(delay)

def get_ping_numbers():
    ping_numbers = input("Enter number of 'ping' messages:")
    return int(ping_numbers)

send(get_client_id(), get_delay(), get_ping_numbers())