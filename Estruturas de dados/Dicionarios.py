
usuario = {"Nome": "Victor", "Email": "exemplo@gmail.com", "Senha": "23455"}

# Adicionar elemento
usuario["telefone"] = "3252-9199"

print(usuario)
print(usuario["Email"])
print(usuario["Nome"])

# Dicionários podem receber diveros valores associados as chaves
nomes = ["João","Carlos","José"]
tupla = ("HS23", "HS24", "HS25")
dados = dict(id = tupla, nomes = nomes)
print(dados)
print(f"{dados['id'][0]} - {dados['nomes'][0]}")

# Interando com for
print(usuario.keys())
print(usuario.values())

for chave in usuario:
    print(f"{chave}: {usuario[chave]}")

for chave, valor in usuario.items():
    print(f"{chave} - {valor}")


# Métodos

print(usuario.get("Senha"))     # Procurar valor da chave
print(usuario.get("Idade", {})) # resposta personalisada quando a chave não existir

usuario.pop("telefone")         # deletar item
print(usuario.pop("Idade", "Elemento não está presente"))   # resposta personalisada na hora de eliminar um item

print(usuario.setdefault("Nome", "Carolina"))                      # Adiciona uma chave caso ela não exista
