
# if básico
saque = int(input("Quanto você deseja sacar? "))
saldo = 1000

if saldo <= saque:
    print("Saque realizado com sucesso!")

if saque > saldo:
    print("Saldo insufisciente!")

# if/else

if saque <= saldo:
    print("Saque realisado com sucesso!")
else:
    print("Saldo insuficiente!")

# if/elif/else

print('''
    1 - Sacar
    2 - Consultar saldo
    3 - sair
''')

operacao = int(input("Informe sua Operação: "))

if operacao == 1:
    saque = int(input("Quanto você deseja sacar? "))
    saldo = 1000

    if saque <= saldo:
        print("Saque realisado com sucesso!")
    else:
        print("Saldo insuficiente!")

elif operacao == 2:
    print(f"Saldo total: {saldo}")

elif operacao == 3:
    print("Operacao finalizada!")

else:
    print("Opção inválida")

# If ternário

idade = int(input("Informe sua idade: "))
status = "Liberado" if idade >= 18 else "Não liberado"
print(f"Usuário {status}")