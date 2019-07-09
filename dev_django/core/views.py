from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(request, nome, idade):
    return HttpResponse(f'Hello {nome}, sua idade é {idade}')
def soma(request, num1, num2):
    return HttpResponse(f'A soma de {num1} e {num2} é {num1+num2}')