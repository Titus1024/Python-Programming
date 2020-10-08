#!/usr/bin/env python3
Octet1 = input("Enter a number between 1 and 255: ")
Octet2 = input("Enter a number between 1 and 255: ")
Octet3 = input("Enter a number between 1 and 255: ")
Octet4 = input("Enter a number between 1 and 255: ")

def IPAddress(Oct1,Oct2,Oct3,Oct4):
    print(f"{Oct1}.{Oct2}.{Oct3}.{Oct4}")

IPAddress(Octet1,Octet2,Octet3,Octet4)