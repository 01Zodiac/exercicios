lista = []
dado = []
opc = ""
mai = men = 0
i = 1
while opc != "N":
    dado.append(input(f"Digite o nome da pessoa {i}: "))
    dado.append(int(input(f"Digite o peso da pessoa {i}: ")))
    i += 1
    if len(lista) == 0:
        mai = men = dado[1]
    else:
        if dado[1] > mai:
            mai = dado[1]
        if dado[1] < men:
            men = dado[1]
    lista.append(dado[:])
    dado.clear()
    opc = input("Quer continuar? [S / N]: ").upper()
    if opc not in "SN":
        print("Escolha apenas entre [S] ou [N]")
        break
if opc == "N":
    if len(lista) < 2:
        print("Foi cadastrada apenas 1 pessoa.")
    else:
        print(f"Foram cadastradas {len(lista)} pessoas.")
    print(f"O maior peso foi de {mai}Kg. Peso de ", end="")
    for p in lista:
        if p[1] == mai:
            print(f"[{p[0]}] ", end="")
    print(f"\nO menor peso foi de {men}Kg. Peso de ", end="")
    for p in lista:
        if p[1] == men:
            print(f"[{p[0]}] ", end="")