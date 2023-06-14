import socket

password = "abc"

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

address = ('127.0.0.1', 2023)

server_socket.bind(address)

server_socket.listen()
print(f'Server is listening on port 2023')

client_id = 0

while True:

    client_id += 1
    brojac = 1
    correct_password = False
    if client_id != 1:
        pick = input('Y/n : ')
        if pick == 'n' or pick == 'N':
            server_socket.close()
            print(f'Client is stopped.')
            break
    client_socket, client_address = server_socket.accept()

    client_socket.send(f'Client {client_id}, welcome'.encode())
    print(f'Client with ID {client_id} is connected')

    if not correct_password:
        for i in range(3):
            recieved_password = client_socket.recv(1024).decode()
            if recieved_password == password:
                print('Correct password')
                correct_password = True
                status = 'correct'
                client_socket.send(status.encode())
                break 
            elif brojac == 3:
                print('Wrong password')
                status = 'wrong'
                client_socket.send(status.encode())
                print('Connection terminated')
                client_socket.close()
                break
            elif recieved_password != password:
                print('Try again: ')
                status = 'again'
                client_socket.send(status.encode())
                brojac += 1
                continue
    # print('ovde sam')
    print(correct_password)
    if correct_password:
        # print('Usao sam ovde')
        while True:
            recieved_message = client_socket.recv(1024).decode()
            if recieved_message == 'exit':
                print('Connection terminated')
                client_socket.close()
                break
            print(f'Clients message: {recieved_message}')

            if client_id % 2 == 0:
                client_socket.send(recieved_message.upper().encode())
                print(f'Sent message to client: {recieved_message.upper()}')
            
            else:
                client_socket.send(recieved_message.lower().encode())
                print(f'Sent message to client: {recieved_message.lower()}')


