import random
jogos = int(input("Quantos jogos você quer que eu sorteie? "))
if jogos > 1:
    print(f"SORTEANDO {jogos} JOGOS")
elif jogos == 1:
    print("SORTEANDO 1 JOGO")
else:
    print("Número de jogos inválido.")
for i in range(1, jogos + 1):
        bot = random.sample(range(1, 60), 6)
        bot.sort()
        print(f"Jogo {i}: {bot}")