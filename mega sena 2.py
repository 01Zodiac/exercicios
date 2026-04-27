import random
lista = list()
jogos = list()
quantidade = int(input('Quantos jogos você quer que eu sorteie? '))
total = 1
while total <= quantidade:
    cont = 0
    while True:
        numero = random.randint(1, 60)
        if numero not in lista:
            lista.append(numero)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
for i, listasjogo in enumerate(jogos):
    print(f'Jogo {i + 1}: {listasjogo}')
print("Boa sorte!")