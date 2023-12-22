
from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime

# Iniciando modelagem de classes para criar o sistema

# Classe abstrata transação para ser usada como base para saque e depósito
class Transacao(ABC):
    # Definir a função como uma propriedade da classe
    @property
    @abstractproperty
    def valor_operacao(self):
        pass

    @abstractclassmethod
    def registrar(self,conta):
        pass

# Criando classe de depósito
class Deposito(Transacao):

    def __init__(self, valor):
        self.valor = valor

    @property
    def valor_operacao(self):
        return self.valor
    
    def registrar(self, conta): # conta é um objeto a ser usada como parametro
        conta.depositar(self.valor) # chamar um método de conta para depositar

# Criando a classe de saque
class Saque(Transacao):

    def __init__(self, valor):
        self.valor = valor
    
    @property
    def valor_operacao(self):
        return self.valor

    def registrar(self, conta): # Conta é um objeto a ser passado como parametro
        conta.sacar(self.valor) # chamar o método de conta para sacar

# A classe histórico registra os dados de transação feita em depósito e saque
class Historico():

    def __init__(self):
        self.transacoes = []    # lista para armazenar as transações
    
    def registrar_transacao(self, transacao):       # Transação é uma instancia de depósito ou saque
        self.transacoes.append({"Tipo":transacao.__class__.__name__,    #nome da transação
                                "Valor": transacao.valor_operacao,      #valor obtido da propriedade da transação
                                "Data": datetime.now().strftime("%d/%m/%Y %H:%M:%S")}) # Data da transação  
        print('Transação concluida!')

# Classe que vai criar um objeto conta a ser usado em depósito e seque
class Conta():
    # Informações da conta
    def __init__(self, agencia, saldo, historico):
        self.agencia = agencia
        self.historico = historico
        self.saldo = saldo
    
    # Criar uma nova conta com um cliente e um número
    def criar_conta(self, cliente, numero):
        self.cliente = cliente  # cliente é um objeto do tip cliente a ser passado como parametro
        self.numero = numero
        print('Conta criada com sucesso!')

    # Metodo chamado na classe Depósito
    def depositar(self, valor):

        if valor <= 0:
            print('Valor inválido!')
        
        else:
            self.saldo += valor
            print('Depósito realizado com sucesso!')
    
    # Método chamado na classe Saque
    def sacar(self, valor):

        if valor > 0:
            self.saldo -= valor
            print('Saque realizado com sucesso!')


# Classe que herda a conta e será usada para criar o objeto conta nas classes depósito e saque
class ContaCorrente(Conta):

    def __init__(self,agencia, saldo, historico, limite, limite_saque):
        super().__init__(agencia, saldo, historico)
        self.limite = limite
        self.limite_saque = limite_saque
    
    # Método usado para validar o saque
    def validar_saque(self, valor):
        numero_saques = [transacao for transacao in self.historico.transacoes if transacao['Tipo'] == "Saque"]

        if self.limite < valor:
            print("O peração falhou. O valor informado está acima do permitido!")
            return False
        
        elif self.saldo < valor:
            print('Saldo insuficiente!')
            return False
        
        elif len(numero_saques) >= self.limite_saque:
            print('Você atingiu a cota de saques por hoje!')
            return False
        else:

            return True
    
    # Método para realizar a transação
    def efetuar_transacao(self, conta, transacao):  # transação é uma instancia de depósito ou saque, conta é o objeto instanciado da própria conta
        transacao.registrar(conta)      # Passando o objeto conta para a transação
        conta.historico.registrar_transacao(transacao)  # registrando os dados da transação no histórico
    
# Classe que cria o objeto cliente
class Cliente():

    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []
    
    def registrar_conta(self, conta):   # Esse método armazena a conta criada no objeto cliente
        self.contas.append(conta)
        print('Conta registrada com sucesso!')

# Classe a ser usada para instanciar o cliente
class PessoaFisica(Cliente):

    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
    
