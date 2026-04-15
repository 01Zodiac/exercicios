maior = h = m20 = 0
i = 1
while True:
    id = int(input(f"Idade {i}? "))
    if id < 0:
        continue
    sexo = " "
    while sexo not in "MF":
        sexo = input(f"Sexo {i}?[M / F] ").strip().upper()[0]
    if id > 17:
        maior += 1
    if sexo == "M":
        h += 1
    if id < 20 and sexo == "F":
        m20 += 1
    op = " "
    while op not in "SN":
        op = input(f"Quer continuar?[S / N] ").strip().upper()[0]
    if op == "N":
        break
    else:
        i += 1
print(f"A quantidade de pessoas de maior é {maior}")
print(f"A quantidade de homens é {h}")
print(f"A quantidade de mulheres com menos de 20 anos é {m20}")
print("\nSaindo do programa...")