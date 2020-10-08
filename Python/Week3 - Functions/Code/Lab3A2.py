#!/usr/bin/env python3
Number = int(input("Enter a number (0-9): "))
def Addition(input):
    add = input + 10
    return add
def Subtraction(input):
    subtract = input - 10
    return subtract
def Multiplication(input):
    multiply = input * 10
    return multiply
def Division(input):
    divide = input / 10
    return divide

print(Addition(Number))
print(Subtraction(Number))
print(Multiplication(Number))
print(Division(Number))