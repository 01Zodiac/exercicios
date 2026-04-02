#Fórmula:  \033[_;__;__m  ...  \033[m
#Estilo: 0, 1 negrito, 4 sublinhado, 7 inverso
#Texto: 30, 31 vermelho, 32 verde, 33 amarelo, 34 azul, 35 roxo, 36 ciano, 37 cinza
#Fundo: 40, 41 vermelho, 42 verde, 43 amarelo, 44 azul, 45 roxo, 46 ciano, 47 cinza

print('\033[0;32;41mOlá Mundo!\033[m')
print('\033[1mOlá Bilsons!\033[m')
print('\033[0;46mOlá Terrestres!\033[m')
print('\033[33mOlá Lucas!\033[m')
nome = input("Qual seu nome? ")
print(f'Olá Sr(a). \033[4;36m{nome}\033[m!!')
a = int(input("Número 1: "))
b = int(input("Número 2: "))
resultado = a + b
print(f"\033[46m{a}\033[m + \033[41m{b}\033[m = \033[44m{resultado}\033[m")