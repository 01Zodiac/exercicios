dado = dict()
partidas = list()
time = list()
while True:
    dado.clear()
    partidas.clear()
    dado["nome"] = input("Nome do jogador: ")
    tot = int(input(f"Quantidade de partidas jogadas por {dado["nome"]}: "))
    for i in range(1, tot + 1):
        partidas.append(int(input(f"Quantidade de gols na partida {i}: ")))
    dado["gols"] = partidas[:]
    dado["total"] = sum(partidas)
    time.append(dado.copy())
    while True:
        opc = input("Quer continuar? [S / N]: ").upper()[0]
        if opc in "SN":
            break
        else:
            print("Opção inválida.")
    if opc == "N":
        break
print("\nnum    nome    gols    total")
for k, v in enumerate(time):
    print(k, end="    ")
    for d in v.values():
        print(d, end="")
    print()


while True:
    esc = int(input("Mostrar dados de qual jogador? [999 para parar]: "))
    if esc == 999:
        break
    elif esc >= len(time):
        print("Jogador inexistente.")
    else:
        print(f"   -- LEVANTAMENTO DO JOGADOR {time[esc]['nome']}:")
        for k, v in enumerate(time[esc]["gols"]):
            print(f"   No jogo {k+1} fez {v} gols.")
    """for i in range(0, len(time[esc]["gols"])):
        print(f"Na partida {i + 1}, fez {time[esc]["gols"][i]} gols.")"""