

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

Informe a operação desejada -> 
"""

while True:
    operacao = int(input(menu))

    if operacao == 1:
        deposito = float(input("Informe o valor a ser depositado -> "))

        if deposito < 0:
            print("Valor inválido")
        
        else:
            print("Depósito realizado com sucesso!")
            saldo += deposito

            extrato += f"""
    Operação: Depóstio
    ->  Valor:  R${deposito}
    ->  Total na conta: R${saldo}

    """
    elif operacao == 2:
        saque = float(input("Informe o valor a ser sacado -> "))

        if saque <= 0:
            print("Valor inválido!")
        
        elif saque > saldo:
            print("Saldo insuficiente!")
        
        elif saque > limite:
            print("Valor de saque acima do limite permitido de R$ 500.0")
        
        elif numero_saques >= 3:
            print("Você esgotou o limite de 3 saques por dia!")
        
        else:
            print("Saque realizado com sucesso")
            saldo -= saque
            numero_saques += 1

            extrato += f"""
    Operação: Saque 0{numero_saques}
    -> Valor:   R${saque}
    -> Total na conta:  R${saldo}

    """

    elif operacao == 3:
        print(extrato)


    elif operacao == 4:
        break

    else:
        print("Operação inválida!")
