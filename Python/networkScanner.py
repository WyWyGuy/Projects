import socket
import _thread
from time import sleep

#Network Information
print("Please enter an IP Address to scan.")

network = "192.168.1."
target = network

print("Scanning: " + target)

#Scan Function
def scan(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex((target + str(ip), port))
    if result == 0:
        print("IP: " + target + str(ip) + ", Port: " + str(port) + " Open\n")
    #else:
        #print("IP: " + target + str(ip) + ", Port: " + str(port) + " Closed\n")
    s.close()

#Loop creating threads
for ip in range(0, 256):
    for port in range(0, 65536):
        _thread.start_new_thread(scan, (ip, port))
        sleep(0.01)
    sleep(10)
sleep(10)
print("Scan Complete!")