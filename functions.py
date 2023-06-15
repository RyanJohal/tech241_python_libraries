# Functions

# code block that can be reused later in the program

# DRY

# Creating a function

# def print_something(print_string):
#     print(print_string)
#
# print_something("This is a string")


# Greeting function

# def greeting(name):
#     print("Hello, my name is " + name)
#
# greeting("Ryan")
# greeting("Parichat")


# Return statement

# def addition(int1, int2):
#     return int1 + int2 #return statement
#
# print(addition(2, 10))

# Default arguments/parameters
# def addition(int1=2, int2=2):
#     return int1 + int2 #return statement
#
# print(addition())
# print(addition(20, 10))
#
# # Multiple agruments
#
# def multi_args(*multiargs):
#     print(type(multiargs))
#
#     for arg in multiargs:
#         print(arg)
#
# multi_args(1, 2, 3, 4, 5)
# print("Break")
# multi_args(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
#


def addition(int1=2, int2=2):
     return int1 + int2

print(addition())

def subtract(int1=10, int2=2):
    return int1 - int2

print(subtract())

def multiply(int1=10, int2=2):
    return int1 * int2

print(multiply())

def divide(int1=10, int2=2):
    return int1 / int2


print(divide())