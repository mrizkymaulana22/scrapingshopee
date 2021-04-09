# import json
import socket
import requests
from bs4 import BeautifulSoup


# Define socket host and port
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 5000

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)
print('Listening on port %s ...' % SERVER_PORT)

while True:
    # Wait for client connections
    client_connection, client_address = server_socket.accept()

    # Get the client request
    request = client_connection.recv(1024).decode()
    print(request)

    #open start.json
    # hghgh
    # fin = open('start.json')
    # Konten = json.load(fin)
    # ktn = json.dumps(Konten)
    # fin.close()

    # url = requests.get('https://detik.com')
    # data = url.text

    url = 'https://detik.com/'

    req = requests.get(url)

    html_parse = BeautifulSoup(req.text, "html.parser")

    data = html_parse.find('h2', class_='box__title')

    print(data)
    # Send HTTP response
    response = f'HTTP/1.0 200 OK\nContent-Type: text-json\n\n{data}'
    client_connection.sendall(response.encode())
    client_connection.close()

# Close socket
server_socket.close()