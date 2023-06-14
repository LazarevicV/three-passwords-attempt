import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

address = ('127.0.0.1', 2023)

client_socket.connect(address)

init_message = client_socket.recv(1024).decode()
print(f'Server sent a message: {init_message}')

for i in range(3):
    correct = False
    password = input('Enter a password: ')
    client_socket.send(password.encode())
    status = client_socket.recv(1024).decode()

    if status == 'correct':
        print('Correct password')
        correct = True
        break
    elif status == 'wrong':
        print('Connection terminated because of wrong password')
    elif status == 'again':
        print('Wrong password, try again client')
        continue

if correct:
    while True:

        message = input('Enter a message: ')
        client_socket.send(message.encode())

        if message == 'exit':
            break

        recieved_message = client_socket.recv(1024).decode()
        print(f'Servers message: {recieved_message}')
    
client_socket.close()
print('Connection terminated')