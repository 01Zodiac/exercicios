# De cinco pesos digitados(Kg) mostra qual dos cinco é mais pesado e mais leve
peso = []
for i in range(1, 6):
    pesos = float(input(f"Digite o peso em kilos da pessoa {i}: "))
    peso.append(pesos)
pesado = max(peso)
leve = min(peso)
print(f"O mais pesado pesa {pesado}. O mais leve pesa {leve}")
