from http import client
import socket
import threading

#Deklarasi IP dan Port Server
host = '127.0.0.1'
port = 5553

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

#Deklarasi Client dan Nama pengguna
clients = []
namax  = []

#Broadcast pesan ke semua client yang terhubung
def broadcast(pesan):
    for client in clients:
        client.send(pesan)

#   
def handle(client):
    while True:
        try:
            pesan = client.recv(1024)
            broadcast(pesan)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nama = namax[index]
            broadcast(f'{nama} Meninggalkan room obrolan!'.encode('ascii'))
            namax.remove(nama)
            break

#Method penerima pesan
def receive():
    while True:
        client, address = server.accept()
        print(f'Terkoneksi dengan IP : {str(address)}')

        client.send('NAMA' .encode('ascii'))

        nama = client.recv(1024).decode('ascii')

        namax.append(nama)
        clients.append(client)

        print(f'Nama Pengguna adalah {nama}')
        broadcast(f'{nama} Bergabung ke dalam obrolan'.encode('ascii'))
        client.send('Terkoneksi dengan TCP Server'.encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("Menunggu Koneksi....")
receive()
