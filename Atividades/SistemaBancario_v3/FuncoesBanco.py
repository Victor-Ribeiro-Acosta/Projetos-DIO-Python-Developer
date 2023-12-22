
import SistemaBancario_03_inteligencia as sbi
from random import choice

def criar_usuario():
    """
    Essa função cria automaticamente um objeto usuario usando a classe PessoaFisica, solicitando os parametros ao usuario
    """
    cpf = str(input('Informe seu CPF -> '))
    nome = str(input('Informe seu nome -> '))
    data_nascimento = str(input('Informe sua data de nascimento -> '))
    endereco = str(input('Informe seu endereço -> '))

    usuario = sbi.PessoaFisica(cpf, nome, data_nascimento, endereco)
    return usuario

def criar_numero_conta():
    """
    Essa função cira automaticamente um número para a conta, com todas as especificações exigidas
    """
    numero_conta = []
    for numero in range(6):
        if numero == 4:
            numero_conta.append('-')
        else:
            numero_conta.append(str(choice(range(0,9))))
    
    return ''.join(numero_conta)

def criar_conta(usuario, numero):
    """Essa função cria um objeto conta.
    Ela recebe o usuario (que é um objeto pessoa física) e um número (criado pela função criar_numero_conta())
    """
    conta = sbi.ContaCorrente("0001", 0, sbi.Historico(), 500, 3) # criando o objeto conta
    conta.criar_conta(usuario, numero)  # vinculando conta ao usuario
    return conta

def procurar_usuario(lista_usuarios, cpf):
    """Essa função procura por um usuario específico dentro de um conjunto de usuarios"""

    usuario = [usuario for usuario in lista_usuarios if usuario.cpf == cpf] # Buscar usuario por meio do cpf
    return usuario[0] if usuario else None  # retornar o valor da lista de usuario se ele existir

def procurar_conta(usuario):
    """Essa função recebe o usuario da função procurar_usuario() e busca por todas as contas vinculadas ao seu cpf"""
    # Validar procura das contas
    if not usuario:
        return None
    
    elif usuario.contas == []:
        return None
    
    else:
        # Listar contas vinculadas ao cpf
        for conta in usuario.contas:
            print(conta.numero)
    
        num_conta = str(input('Informe o número da conta: '))   # solicitar o número daconta
        conta = [conta for conta in usuario.contas if conta.numero == num_conta]    # buscar a conta com o número indicado
        return conta[0] if conta else None  # Retorne o valor de conta se ela existir

def depositar(lista_usuarios):

    cpf = str(input('Informe seu cpf: '))
    # Buscar usuario cadastrado (caso não exista, anuncia-rá)
    usuario = procurar_usuario(lista_usuarios, cpf)
    if not usuario:
        print('Usuário não cadastrado!\nOperação falhou.')
        return
    # Se o usuario existir, buscar contas vinculadas ao cpf
    conta = procurar_conta(usuario)

    # Caso o usuario não tenha conta, anuncia-rá
    if not conta:
        print('Usuário sem conta cadastrada!\nOperaçao falhou.')
        return

    # Informar valor de deposito
    valor = float(input('Informe o valor de depósito'))

    transacao = sbi.Deposito(valor) # criar objeto transação
    conta.efetuar_transacao(conta, transacao)   # efetuar transação (analisar método na classe ContaCorrente)

def sacar(lista_usuarios):

    cpf = str(input('Informe seu cpf: '))
    # Procurar usuario pelo cpf
    usuario = procurar_usuario(lista_usuarios, cpf)

    # Caso o usuario não exista, avisar
    if not usuario:
        print('Usuário não cadastrada!\nOperação falhou.')
        return
    
    # Se o usuario existir, procurar as contas vinculadas ao seu cpf
    conta = procurar_conta(usuario)

    #Se a conta não existir, avisar
    if not conta:
        print('Usuário sem conta registrada!\nOperação falhou.')
        return
    
    # Se a conta existir, informar valor de saque
    valor = float(input('Informe o valor de saque: '))
    
    if conta.validar_saque(valor):  # validar valor de saque
        transacao = sbi.Saque(valor)    # criar objeto transação
        conta.efetuar_transacao(conta, transacao)   # efetuar transação (analisar método na classe ContaCorrente)
        print('Transaçao realizada com sucesso!')


