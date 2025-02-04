#!/usr/bin/env python3

def greet_programmer():
    print ("Hello, programmer!")
    pass

def greet(name):
    print(f"Hello, {name}!")

greet("Naureen")
pass

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

greet_with_default() 
greet_with_default("Sunny")  
pass

def add(num1, num2):
    return num1 + num2

sum = add(1, 2)
print(sum)
pass

def halve(number):
    if not isinstance(number, (int, float)):
        return None
    
    return number / 2
pass
