
# São imutáveis

tp = ("Anderson", "Carlos", "Diego")
#tp.append("Jorge") não pode

# Criando tuplas com palavras
letras = tuple("python",)   # usar vírgula para identificar tupla e não precedencia de operadores
print(letras)

# Fatiamento de tuplas
print(letras[0])
print(letras[1:4])
print(letras[:5])
print(letras[4:])

# interando com for
for nome in tp:
    print(nome)

# Condicional
n = "Alberto"
if n in tp:
    print("sim")
else:
    print("não")

# Metodos
tp.count("Diego")
