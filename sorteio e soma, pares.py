import random
from time import sleep


def sorteia(lista):
    print("Sorteando 5 valores da lista: ", end="")
    for i in range(5):
        val = random.randint(1, 10)
        lista.append(val)
        print(val, end=" ", flush=True)
        sleep(0.3)

def somaPar(lista):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
    print(f"\nSomando os valores pares de {lista}, temos {soma}")

lista = list()
sorteia(lista)
somaPar(lista)