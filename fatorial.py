# Mostra a fatorial de um número por extenso
import math as m
num = int(input("Digite um número: "))
i = num
print(f"{num}!")
while i > 0:
    print(i, end="")
    if i > 1:
        print("x ", end="")
    else:
        print("x =", end="")
    i -= 1
print(f" {m.factorial(num)}")