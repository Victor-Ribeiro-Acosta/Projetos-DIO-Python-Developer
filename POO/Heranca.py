
class veiculo():
    def __init__(self, num_rodas, marca, num_passageiros, placa):
        self.n_rodas = num_rodas
        self.marca = marca
        self.n_passag = num_passageiros
        self.placa = placa

    def informar_veiculo(self):
        return f"{', '.join([f"{chave} - {valor}" for chave, valor in self.__dict__.items()])}"




class motocicleta(veiculo):

    def dar_partida(self):
        print('Moto ligada...')



class carro(veiculo):
    def __init__(self, num_rodas, marca, num_passageiros, placa, n_marchas):
        super().__init__(num_rodas, marca, num_passageiros, placa)
        self.numero_marchas = n_marchas

    def ligar_carro(self):
        print('Carro ligado.\nEngatando primeira marcha')



class onibus(veiculo):
    pass



honda = motocicleta(2,'Honda', 1,'byw 9973')
print(honda.informar_veiculo())

embaixador = onibus(6, 'embaixador', 44, 'wwg 4545')
print(embaixador.n_passag)

carro = carro(4, 'Celta', 5, 'htj 2797', 6)
print(carro.informar_veiculo())
print(carro.ligar_carro())