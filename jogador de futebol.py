dado = dict()
partidas = list()
total = 0
dado["nome"] = input("Nome do jogador: ")
tot = int(input(f"Quantidade de partidas jogadas por {dado["nome"]}: "))
for i in range(1, tot + 1):
    partidas.append(int(input(f"Quantidade de gols na partida {i}: ")))
    total += partidas[i - 1]
dado["gols"] = partidas
dado["total"] = total
print()
for k, v in dado.items():
    print(f"   - {k} tem o valor {v}")
print(f"\nO jogador {dado["nome"]} jogou {tot} partidas.\n")
for i in range(1, tot + 1):
    print(f"Na partida {i}, fez {partidas[i - 1]} gols.")