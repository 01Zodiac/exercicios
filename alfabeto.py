# Escreva um programa que leia um número inteiro N e imprima os N primeiros caracteres do alfabeto.

n = int(input("Digite um número: "))

alfabeto = "abcdefghijklmnopqrstuvwxyz"

for i in range(n):
    if i < n - 1:
        print(alfabeto[i], end=",")
    else:
        print(alfabeto[i])