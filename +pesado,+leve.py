# De cinco pesos digitados(Kg) mostra qual dos cinco é mais pesado e mais leve
for i in range(1, 6):
    peso = int(input(f"Digite o peso da pessoa {i}: "))
    if i == 1:
        pesado = leve = peso
    else:
        if peso > pesado:
            pesado = peso
        if peso < leve:
            leve = peso
print(f"O mais pesado pesa {pesado}. O mais leve pesa {leve}")
