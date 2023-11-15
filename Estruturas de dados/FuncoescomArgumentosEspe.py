
#   *args - usado para passar tuplas e listas
#   **args - usado para passar um dicionário

# PARAMETROS ESPECIAIS

    # Parametros de posição: são aqueles que seu valor é definido pela posição do valor informado
    # Parametros nomeados: aqueles cuja variavel do parametro tem seu valor atribuido por meio de uma atribuição chave valor (parametro = valor)
    # Parametros especiais: são formas de tornar tais atribuições opcionais ou não
        # / - exige que todos os parametros anteriores sejam de posição
        # * - exige que todos os parametros após ele sejam nomeados

def operacoes_aritmeticas(numero1, numero2,/, operador):
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

resultado = operacoes_aritmeticas(10,50, operador='/')
#resultado = operacoes_aritmeticas(numero1=10,numero2=50, operador='^')

print(resultado)


def operacoes_aritmeticas2(operador,*,numero1, numero2,):
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

resultado = operacoes_aritmeticas2(operador="-", numero1=100, numero2=30)
#resultado = operacoes_aritmeticas2(operador="-", 100, 30)

print(resultado)