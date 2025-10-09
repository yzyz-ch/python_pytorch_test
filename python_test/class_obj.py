#!/usr/bin/python3

class Complex:
    #define the base value, every obj are the same
    realpart = 0.0
    imagpart = 0.0
    #protect value
    _protectValue = 0.0
    #private value
    __weight =0
    def __init__(self, realpart = 1.6, imagpart = 2.3, __weight = 1.0):
        self.r = realpart
        self.i = imagpart
        self.__w = __weight

    def print(self):
        print("self realpart:", self.r, "imagpart:", self.i, "weight:", self.__w)

x = Complex(3.0, -4.5, 2.0)
y = Complex()
print(x.r, x.i)
print(y.r, y.i)

print(f"print value x.r:{x.r}, y.r:{y.r}")