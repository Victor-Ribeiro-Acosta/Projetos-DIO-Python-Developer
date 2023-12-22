import FuncoesBanco as fb

menu = """
[1] - Criar usuario
[2] - Criar conta
[3] - Depositar
[4] - Sacar
[5] - Consultar saldo
[6] - Sair

Informe sua opção -> """

lista_usuarios = [] # lista para armazenar os usuarios
extrato = "Tipo\t\tValor\t\tData\n" # criar extrato
while True:

    opcao = int(input(menu))    # solicitar uma ação

    # Criar usuario
    if opcao == 1:
        usuario = fb.criar_usuario()
        lista_usuarios.append(usuario)
    
    # Criar conta
    elif opcao == 2:
        cpf = str(input('Informe seu cpf: '))
        usuario = fb.procurar_usuario(lista_usuarios, cpf)
        numero_conta = fb.criar_numero_conta()
        conta = fb.criar_conta(usuario, numero_conta)
        usuario.registrar_conta(conta)

    # Fazer depósito
    elif opcao == 3:

        fb.depositar(lista_usuarios)
    
    # Fazer saque
    elif opcao == 4:

        fb.sacar(lista_usuarios)
    
    # Ver extrato
    elif opcao == 5:
        cpf = str(input('Informe seu cpf: '))
        usuario = fb.procurar_usuario(lista_usuarios, cpf)
        conta = fb.procurar_conta(usuario)

        transacoes = conta.historico.transacoes

        if transacoes == []:
            extrato = "Ainda não foram feitas transações"

        for transacao in transacoes:
            extrato += f"{transacao['Tipo']}\t\t{transacao['Valor']}\t\t{transacao['Data']}\n"
        
        print(extrato)
    
    # Sair do sistema
    elif opcao == 6:
        break

print('>>>  Seção encerrada <<<')

