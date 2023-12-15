from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, sobrenome, produto, preco):
    return HttpResponse(f'''<h1>Hello {nome} {sobrenome}!<h1>
    Bem vindo a nossa loja de artigos esportivos, o produto{produto} custa em torno de R${preco}''')