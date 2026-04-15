# Jogo de par ou ímpar, o computador vai pensar em um número de 1 a 10, se o jogador ganhar ele continua jogando

import random
seq = 0
while True:
    sk = ""
    jogo = ""
    num = int(input("Digite um número: "))
    op = input("Par ou ímpar? [P / I]: ").upper()
    if op != "P" and op != "I":
        print("Opção inválida")
        break
    comp = random.randint(1, 10)
    total = num + comp
    val = total % 2
    if val == 0:
        jogo = "Par"
        sk = "P"
    else:
        jogo = "Impar" 
        sk = "I"
    print(f"Você jogou {num} e o computador {comp}. Total de {total} deu {jogo}")
    if op == sk:
        print("Você ganhou, jogue de novo")  
        seq += 1
    else:
        print(f"Perdeu, sua sequência de vitórias foi {seq}")
        break
print("Saindo do programa...")