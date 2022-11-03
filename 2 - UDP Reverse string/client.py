import socket


def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number

    client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    client_socket.connect((host, port))  # connect to the server

    message = input(" -> ")  # take input

    while message.lower().strip() != 'bye':
        client_socket.sendto(message.encode(), (host, port))  # send message

        data, addr = client_socket.recvfrom(1024)
        data = data.decode() # receive response
        data = data[::-1]
        print('Received from server: ' + data)  # show in terminal

        message = input(" -> ")  # again take input


if __name__ == '__main__':
    client_program()
