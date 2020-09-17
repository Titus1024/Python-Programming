#!/usr/bin/env python3
import keyword
"""
This is a multi
line
comment
"""
keywords = keyword.kwlist
UserInput = input("Hello, what is your name? ")
print(f"Hello, {UserInput}!")
KeywordPrompt = int (input("Do you know how many keywords are in Python? "))
if KeywordPrompt == len(keywords):
    print(str(len(keywords)) + " is correct!")
    print("I leanred that Python has " + str(len(keywords)) + " keywords")
elif KeywordPrompt != len(keywords):
    print(str(KeywordPrompt) + " is incorrect!")