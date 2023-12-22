
# Instaciando classe normalmente
class controleRemoto():
    def ligar(self):
        pass

    def desligar(self):
        pass


class ControleTV(controleRemoto):
    pass

tv = ControleTV()
tv.desligar()
tv.ligar()

# Criando classes abstratas
from abc import ABC, abstractmethod, abstractproperty

class controleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    # Definir uma propriedade obrigatória
    @property
    @abstractproperty
    def bateria_fraca(self):
        pass


class ControleTV(controleRemoto):
    def ligar(self):
        print('Ligando a TV...')
    
    def desligar(self):
        print('Desligando...')
    
    @property
    def bateria_fraca(self):
        return True

tv = ControleTV()
tv.desligar()
tv.ligar()
tv.bateria_fraca