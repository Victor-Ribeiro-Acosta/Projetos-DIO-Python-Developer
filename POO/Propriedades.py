

class poo():
    def __init__(self, a):
        self._a = a         #Variavel que não deve ser alterada
    
    def Fx(self):
        return self._a*2 + 3 or 0
        

poo = poo(2)
print(poo.Fx)


# Usando metodos de depuradores


class poo():
    def __init__(self, a):
        self._a = a         #Variavel que não deve ser alterada

    @property 
    def Fx(self):
        return self._a*2 + 3 or 0
    
    @Fx.setter
    def Sx(self, valor):
        self._a -= (self._a*valor)
        

poo = poo(2)
print(poo.Fx)
poo.Sx = 1
print(poo.Sx)