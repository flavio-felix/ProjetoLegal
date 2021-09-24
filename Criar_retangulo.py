#coding: utf-8

class Retangulo:
    def __init__(self, altura, largura):
        self._altura = 0
        self._largura = 0
        self.set_altura(altura)
        self.set_largura(largura)

    def set_altura(self, num):
        if(not(isinstance(num, int) and (num > 0))):
               raise ValueError("Altura é inválida: {}".format(num))
        self._altura = num

    def set_largura(self, num):
        if(not(isinstance(num, int) and (num > 0))):
               raise ValueError("Largura é inválida: {}".format(num))
        self._largura = num

    def get_area(self):
        return self._altura * self._largura

r = Retangulo(largura=5, altura=10)
print(r.get_area())
