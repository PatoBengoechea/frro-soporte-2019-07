# Implementar la clase Circulo que contiene un radio, y sus métodos area y perimetro.

import math

class Circulo:


    def __init__(self, radio):
        self.r = radio

    def area(self):
        a = math.pi * math.pow(self.r, 2)
        return a

    def perimetro(self):
        per = 2 *math.pi * self.r
        return per

a = Circulo(5)
assert (a.perimetro() == 31.41592653589793)
assert (a.area() == 78.53981633974483)


