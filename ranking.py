import time
import random
import operator
jogos = dict()
print("Valores sorteados:")
time.sleep(1)
for i in range(1, 5):
    jogos[f"jogador{i}"] = random.randint(0, 10)
    print(f"Jogador {i} tirou: {jogos[f"jogador{i}"]}")
    time.sleep(1)
print("vvv   Ranking dos jogadores   vvv")
ordem = sorted(jogos.items(), key=operator.itemgetter(1), reverse=True)
for i in range(0, 4):
    print(f"{i+1}º lugar {ordem[i][0]} com {ordem[i][1]}")
    time.sleep(1)
