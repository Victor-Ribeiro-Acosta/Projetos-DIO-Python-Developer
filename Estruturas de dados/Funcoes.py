
# Declarando uma função
def mensagem():

    print("Olá mundo")

# função com argumentos
def soma(numero1, numero2):
    s = numero1 + numero2
    print(f"A soma de {numero1} com {numero2} é {s} ")

# Retornando valores

def operacoes_aritmeticas(numero1, operador, numero2):

    if operador == '+':
        return numero1 + numero2

    elif operador == "-":
        return numero1 - numero2

    elif operador == "*":
        return numero1 * numero2
    
    elif operador == "/":
        return numero1 / numero2
    
    elif operador == "^":
        return numero1**numero2
    
    else:
        return "Operação inválida"
