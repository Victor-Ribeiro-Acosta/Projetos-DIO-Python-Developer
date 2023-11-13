
palavra = "PyThon"
frase = "olá mundo"

print(palavra.upper())
print(palavra.lower())
print(palavra.capitalize())
print()
print(palavra.center(8,"*"))
print(" ".join(palavra))

print(frase.split())

# interpolação de string
nome = "Victor"
idade = 25
curso = "python"
pessoa = {"nome": "Victor", "idade": 25, "curso": "Python"}
print("Olá, me chamo %s, tenho %d e estou estudando %s" % (nome, idade, curso))
print("Olá, me chamo {}, tenho {} e estou estudando {}".format(nome, idade, curso))
print("Olá, me chamo {nome}, tenho {idade} e estou estudando {curso}".format(**pessoa))
print(f"Olá, me chamo {nome}, tenho {idade} e estou estudando {curso}")

# Fatiamento de string

print(palavra[1])      #pegar letra de indice 1
print(palavra[1:3])    #pegar todasas letras do intervalo de 1 a 3
print(palavra[2:])     #pegar todas as letras acima do índice 2
print(palavra[:4])     #pegar todas as letras cujo índice seja menor que 4
print(palavra[:])      #cria uma cópia da string
print(palavra[0:4:2])  #Buscar as letras de índice 0 a 4 pulando de 2 em 2
print(palavra[::-1])   #Retorna a string ao contrário

# string com várias linhas
print('''
===============================================

    Bom dia! Seja bem vindo ao nosso jogo.
      
    Informe sua credencial:
      
    - Iniciante:
    - Pró
    - Profissional

===============================================
''')