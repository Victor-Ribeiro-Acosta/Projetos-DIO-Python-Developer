
class conta_bancaria():
    def __init__(self, saldo):
        self.saldo = saldo

    def saque(self, saque):

        if saque < self.saldo:
            self.saldo -= saque

    def deposito(self, deposito):

        if deposito > 0:
            self.saldo += deposito
      

conta = conta_bancaria(100)
print(conta.saldo)
conta.saldo += 100      # não é possível tornar atributos e variáveis restritas em python, assim, elas ficam sucetíveis a alterações
print(conta.saldo)

# Boas práticas para proteger variáveis

    # Manter dentro do escopo da classe

class conta_bancaria():
    def __init__(self, saldo):
        self.saldo = saldo

    def saque(self, saque):

        if saque < self.saldo:
            self.saldo -= saque

    def deposito(self, deposito):

        if deposito > 0:
            self.saldo += deposito

    def mostrar_saldo(self):
        return f"{self.saldo}"      # Esse método mostra o valor de saldo, mas não permite altera-lo


conta = conta_bancaria(1000)
conta.saque(100)
print(conta.mostrar_saldo())


