
lista01 = ["João", "Alberto", "Augusto", "Marcos", "Iohamn"]
lista02 = ["Marcos", 25, 1.88, "M"]
lista03 = []
letras = list("Programação")

print(lista01)
print(lista02)
print(lista03)
print(letras)

# Fatiamento de listas
print(letras[0])
print(lista01[2:4])
print(lista02[3:])
print(lista02[:2])
print(letras[0::3])

# Condicional com lista

if "André" in lista01:
    print("sim")

if "Marcos" in lista01:
    print("sim")


# iterar listas

for letra in letras:
    print(letra, end="")

for i, nome in enumerate(lista01):
    print(f"{i+1} - {nome}")

# List Comprehensios

consoante = [letra for letra in letras if letra.lower() not in "aeiou"]
print(f"As consoantes da palavra são {consoante}")

# Criando string a partir de lista

palavra = "".join(letras)
print(palavra)