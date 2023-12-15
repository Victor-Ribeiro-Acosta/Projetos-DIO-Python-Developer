from random import choice

numero_saques = 0
saldo = 0
limite = 500
extrato = f"""
================================
        Extrato Bancário
================================

-> Total em conta: R${saldo}

"""

menu = """
Operações:

    [1] - Depositar
    [2] - Sacar
    [3] - Consultar saldo
    [4] - Sair

Informe a operação desejada ->"""


lista_contas = []
lista_usuarios = []


def deposito(valor_deposito, saldo, extrato):

    if valor_deposito < 0:
            print("Valor inválido")
        
    else:
        print("Depósito realizado com sucesso!")
        saldo += valor_deposito

        extrato += f"""
    Operação: Depóstio
    ->  Valor:  R${valor_deposito}
    ->  Total na conta: R${saldo}"""
    
    return saldo, extrato



def sacar(*, valor_saque, numero_saque, saldo, limite, extrato):
    if valor_saque <= 0:
        print("Valor inválido!")
        
    elif valor_saque > saldo:
        print("Saldo insuficiente!")
        
    elif valor_saque > limite:
        print("Valor de saque acima do limite permitido de R$ 500.0")
        
    elif numero_saque >= 3:
        print("Você esgotou o limite de 3 saques por dia!")
        
    else:
        print("Saque realizado com sucesso")
        saldo -= valor_saque
        numero_saque += 1

        extrato += f"""
    Operação: Saque 0{numero_saques}
    -> Valor:   R${valor_saque}
    -> Total na conta:  R${saldo}

    """
        
def mostra_extrato(saldo,/,*,extrato):
    print(extrato)


def criar_usuario(cpf, lista_usuarios, lista_contas):
    usuario = {}
    dados_num_conta = []
    conta_usuario = {}
    dados_agencia = '0001'

    if len(cpf) != 11:
        print("O cpf informado não é válido")
    
    else:
        nome = str(input('Informe seu nome-> '))
        data_nascimento = str(input('Informe sua data de nascimento-> '))
        endereco = str(input('Informe seu endereço completo->'))

        usuario['cpf'] = cpf
        usuario['dados'] = {"data_nascimento":data_nascimento, "nome":nome, "endenreco": endereco}


        lista_usuarios.append(usuario)

        for num in range(6):
            if num == 4:
                dados_num_conta.append('-')

            else:
                dados_num_conta.append(str((choice(range(9)))))
        

        conta_usuario = {"agencia":dados_agencia, "numero":''.join(dados_num_conta), "usuario": nome, "cpf":cpf}
        lista_contas.append(conta_usuario)
        return f"""
        agencia: {conta_usuario['agencia']}
        conta:  {conta_usuario['numero']}
        nome:   {conta_usuario['usuario']}"""



def conta(agencia, numero, contas):
        
    if len(numero) != 6:
        print('Numero de conta inválida')

    elif numero[4] != '-':
        print('Sua conta deve conter um - para separa o dígito final!')
    
    else:

        for conta in contas:
            if conta["agencia"] == agencia and conta["numero"] == numero:
                print(f"Bem vindo {conta["usuario"]}")
                return True
            
            else:
                print("Agencia ou número não encontrado!")
        return False








# Sistema
while True:

    print('Para encerrar processo, digite "sair" ')
    respota_conta = str(input('Você já é nosso cliente [sim/não]-> '))

    if respota_conta.lower() == "sair":
        break


    if respota_conta.lower() == 'sim':
        numero_agencia = str(input('Informe o número da agencia-> '))
        numero_conta = str(input("Informe o número da conta -> "))

        if conta(numero_agencia, numero_conta, lista_contas):

            while True:
                operacao = int(input(menu))

                if operacao == 1:
                    valor = float(input('Informe o valor a ser depositado -> '))
                    deposito(valor, saldo, extrato)
                
                elif operacao == 2:
                    saque = float(input('Informe o valor de saque -> '))
                    sacar(valor_saque=saque, numero_saque=numero_saques, saldo=saldo, limite=limite, extrato=extrato)
                
                elif operacao == 3:
                    mostra_extrato(saldo, extrato=extrato)
                
                elif operacao == 4:
                    break

                else:
                    print('Opção inválida!')

    elif respota_conta.lower() == 'não':
        cpf = str(input("Digite seu cpf sem [.] ou [-] -> "))
        informacao_conta = criar_usuario(cpf, lista_usuarios, lista_contas)
        print(informacao_conta)

    else:
        print('Opção inválida!')


