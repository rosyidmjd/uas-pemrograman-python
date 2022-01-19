import socket
import threading

nama = input("Nama anda: ")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 5553))

#Method penerima dan print pesan
def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NAMA':
                client.send(nama.encode('ascii'))
            else:
                print(message)
        except:
            print("Ada yang error nih!")
            client.close()
            break

def write():
    while True:
        message = f'{nama}: {input("")}'
        client.send(message.encode('ascii'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
