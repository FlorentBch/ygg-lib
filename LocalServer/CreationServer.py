import socket
import os

def start_server(host, port, shared_folder):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print(f"Serveur en écoute sur {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connexion établie avec {client_address}")

        request = client_socket.recv(1024).decode('utf-8')

        if request == 'list':
            file_list = os.listdir(shared_folder)
            file_list_str = "\n".join(file_list)
            client_socket.send(file_list_str.encode('utf-8'))
        elif request.startswith('get'):
            _, file_name = request.split(' ', 1)
            file_path = os.path.join(shared_folder, file_name)

            if os.path.exists(file_path):
                with open(file_path, 'rb') as file:
                    content = file.read()
                    client_socket.send(content)
            else:
                client_socket.send(b'File not found')

        client_socket.close()

# if __name__ == "__main__":
#     host = '0.0.0.0'  # Écoute sur toutes les interfaces réseau
#     port = 12345  # Port d'écoute
#     shared_folder = 'C:/Users/florent/Documents/ygg-lib/Data/Top Films SC'

#     start_server(host, port, shared_folder)


def get_file_list(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    client_socket.send(b'list')
    file_list = client_socket.recv(1024).decode('utf-8')

    print(f"Liste des fichiers:\n{file_list}")

    client_socket.close()

if __name__ == "__main__":
    host = '192.168.1.16'  # Remplacez par l'adresse IP réelle du serveur
    port = 12345

    get_file_list(host, port)
