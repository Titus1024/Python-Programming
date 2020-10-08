#!/usr/bin/env python3
Fahrenheit = float(input("Enter a temperature in Fahrenheit: "))

def ConvertTo(f):
    output = (f - 32) * 5/9
    return output

print(f"Temperature in Celsius: {ConvertTo(Fahrenheit)}")