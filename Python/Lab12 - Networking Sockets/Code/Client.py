#!/usr/bin/env python3
import socket

HOST = '192.168.1.70'    # The target IP address
PORT = 5000     # Target Port number
DATA = (input('Enter Text: '))
#HEXDATA = '\x90\x90\x90\x90\x90\x90'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.send(DATA)  # Put the pattern you want to send here.
data = s.recv(1024)
s.close()
