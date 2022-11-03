import socket


def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 5000  # initiate port no above 1024

    server_socket = socket.socket(family = socket.AF_INET, type = socket.SOCK_DGRAM)  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data, addr = server_socket.recvfrom(1024)
        data = data.decode()
        if not data:
            # if data is not received break
            break
        data = data[::-1]
        print("from connected user: " + str(data))
        data = input(' -> ')
        server_socket.sendto(data.encode(), addr)  # send data to the client


if __name__ == '__main__':
    server_program()