maior = h = m20 = 0
i = 1
while True:
    id = int(input(f"Quantos anos tem a pessoa {i}? "))
    if id < 0:
        print("Idade inválida")
        break
    sexo = input(f"Qual é o sexo da pessoa {i}?[M / F] ").strip().upper()[0]
    if sexo != "M" and sexo != "F":
        print("Sexo inválido")
        break
    if id > 17:
        maior += 1
    if sexo == "M":
        h += 1
    if id < 20 and sexo == "F":
        m20 += 1
    op = input("Quer continuar?[S / N] ").strip().upper()[0]
    if op == "S":
        i += 1
    elif op == "N":
        print("\nSaindo do programa...")
        break
    else:
        print("Opção inválida")
        break
print(f"A quantidade de pessoas com mais de 17 anos é {maior}")
print(f"A quantidade de homens é {h}")
print(f"A quantidade de mulheres com menos de 20 anos é {m20}")
print("\nSaindo do programa...")