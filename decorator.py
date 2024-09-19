#!/usr/bin/python3
def add(a,b):
    def dec(og_fun):
        def wrapper(*args,**kwargs):
            og_fun(a+b)
        return wrapper
    return dec

def addone(a):
    def dec(og_fun):
        def wrapper(*args,**kwargs):
            og_fun(a+1)
        return wrapper
    return dec

@addone(2)
@add(3,4)
def print_(a):
    print(a)

print_()
