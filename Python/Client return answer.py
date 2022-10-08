#!/usr/bin/python3

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = (("192.168.173.68", 2000))

client.connect(host) # Connect to our client

m1 = client.recv(1024).decode()
print(m1)

mb1 = m1

client.send(mb1.encode())
m2 = client.recv(1024).decode()
print(m2)

mb2 = m2

client.send(mb2.encode())
m3 = client.recv(1024).decode()
print(m3)

mb3 = m3

client.send(mb3.encode())
m4 = client.recv(1024).decode() 
print(m4)

mb4 = m4

client.send(mb4.encode())
m5 = client.recv(1024).decode() 
print(m5)

mb5 = m5 

client.send(mb5.encode())
m6 = client.recv(1024).decode() 
print(m6)

mb6 = m6

client.send(mb6.encode())
m7 = client.recv(1024).decode() 
print(m7)

mb7 = m7

client.send(mb7.encode())
m8 = client.recv(1024).decode() 
print(m8)

mb8 = m8

client.send(mb8.encode())
m9 = client.recv(1024).decode() 
print(m9)

mb9 = m9

client.send(mb9.encode())
m10 = client.recv(1024).decode() 
print(m10)

mb10 = m10

client.send(mb10.encode())
m11 = client.recv(1024).decode() 
print(m11)

client.close()