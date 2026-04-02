#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:
#- Se ele ainda vai se alistar ao serviço militar.
#- Se é a hora de se alistar.
#- Se já passou do tempo do alistamento.

num = int(input("Digite seu ano de nascimento: "))

if num == 2008:
    print("É hora de se alistar")
elif num < 2008:
    print("Passou o tempo de alistamento")
    print("Tempo que passou:", 2008 - num)
elif num > 2008:
    print("Ainda vai se alistar")
    print("Tempo que falta:", num - 2008)
else:
    print("Erro")
