
class Passaro():
    def voar(self):
        print('Esse pássaro voa...')

class Pardal(Passaro):
    def voar(self):         # o método voar se comporta de uma forma em pardal
        super().voar()


class Avestruz(Passaro):
    def voar(self):         # o método voar se comporta de outra maneira em avestruz
        print('Avestruz não voa')

def funcao_voar(obj):
    obj.voar()

funcao_voar(Avestruz())
funcao_voar(Pardal())