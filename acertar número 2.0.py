# Jogo de adivinhar o número entre 0 e 5

import random
import time

comp = random.randint(0, 5)
jogo = int(input("Tente acertar qual número eu pensei, entre 0 e 5: "))
print("PROCESSANDO...")
time.sleep(2)
if jogo == comp:
    print("PARABÉNS! Você acertou!")
else:
    print("ERROU! O número que eu pensei foi {}.".format(comp))
