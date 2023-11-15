
# Elimina valores duplicados

val_unicos = set([1,1,1,2,3,4,5])
print(val_unicos)

# Não obedece a ordem inicial
print({"python", "Java", "php", "python", "ruby", "Java"})

# interando com for
linguagens = set(["python", "Java", "php", "python", "ruby", "Java"])
for ling in linguagens:
    print(ling)

#Operações com conjuntos (conjuntos matemáticos)
A = {1,2,3,4,5,6,7}
B = {3,5,7}
print(A.union(B))       # União
print(A.intersection(B))    # Interseção
print(A.difference(B))      # Diferença
print(A.symmetric_difference(B))
print(A.issubset(B))
print(B.issubset(A))
print(A.isdisjoint(B))

# Metodos

linguagens.add("JavaScript")
print(linguagens)
print(len(linguagens))

linguagens.discard("php")
print(linguagens)