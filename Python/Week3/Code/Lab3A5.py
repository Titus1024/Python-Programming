#!/usr/bin/env python3
Celsius = float(input("Enter a temperature in Celsius: "))

def ConvertTo(c):
    output = (c * 9/5) + 32
    return output

print(f"Temperature in Fahrenheit: {ConvertTo(Celsius)}")