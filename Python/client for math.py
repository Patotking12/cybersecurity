#!/usr/bin/python
import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

conn.connect(("192.168.221.101", 8888))
print(conn.recv(1024).decode())

string = conn.recv(1024).decode().split()
print(string)

num1 = int(list(string)[8])
num2 = int(list(string)[10])
num3 = int(list(string)[12])
total = str((num1 + num2) * num3)
print(total)

conn.send(total.encode()) 
print(conn.recv(1024).decode())

conn.close()