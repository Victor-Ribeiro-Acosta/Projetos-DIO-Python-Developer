
class notebook():
    def __init__(self, placa, marca, mem_ram, ssd, processador, so):     # método construtor, onde os atributos são definidos, é o primeiro método a ser executado
        # Definindo atributos
        self.placa = placa
        self.marca = marca
        self.menmoria_ram = mem_ram
        self.ssd = ssd
        self.prcessador = processador
        self.sist_operacional = so
    
    # Definindo métodos da classe
    def ligar_computador(self):
        print('Ligando computador...')
        return True
    
    def desligar_computador(self):
        print('Computador desligando...')
        return True


lenovo = notebook(620, 'Lenovo', '12 gb', 240, 'Intel core i5', 'Windows11')
# O objeto possui os atributos e métodos da classe
print(lenovo.menmoria_ram)
print(lenovo.prcessador)
lenovo.ligar_computador()

# Propriedades das classes
for k, v in lenovo.__dict__.items():
    print(f"{k} - {v}")

print(lenovo.__class__.__name__)
