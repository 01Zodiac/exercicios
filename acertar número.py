# Jogo de adivinhar o número entre 1 e 5

import random

maquina = random.randint(1, 5)
numero = int(input("Em que número de 1 a 5 eu pensei? "))
if numero == maquina:
    print(f"Acertou, pensei exatamente no número {maquina}")
else:
    print(f"Errou, pensei no número {maquina}")
