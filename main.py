#coding: utf-8

class Primeiro:
    def __init__(self):
        self.var = 0

    def func(self):
        return self.var 

    def entra(self, x):
        self.var = x

p = Primeiro()
p.entra(100)
print(p.func())
