# Jogo de adivinhar o número entre 0 e 5

import random
import time

computador = random.randint(1, 10)
chute = 1
numero = "incorreto"
print("Tente acertar qual número de 0 a 10 eu pensei")
while numero == "incorreto":
    jogo = int(input("Número de 0 a 10: "))
    print("PROCESSANDO...")
    time.sleep(2)
    if jogo == computador:
        numero = "correto"
        print(f"Acertou!! Você chutou {chute}x.")
    elif jogo > 10:
        print("Digite números apenas de 0 a 10.")
    else:
        chute += 1
        print(f"Não é {jogo}, tente outro número.")