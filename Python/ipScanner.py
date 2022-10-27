import socket
import _thread
from time import sleep

#Network Information
print("Please enter an IP Address to scan.")
target = input("> ")

print("Scanning: " + target)

#Scan Function
def scan(port, null):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex((target, port))
    if result == 0:
        print("IP: " + target + ", Port: " + str(port) + " Open\n")
    #else:
        #print("IP: " + target + ", Port: " + str(port) + " Closed\n")
    s.close()

#Loop creating threads
for port in range(0, 65536):
    _thread.start_new_thread(scan, (port, 0))
    sleep(0.005)
sleep(10)
print("Scan Complete!")