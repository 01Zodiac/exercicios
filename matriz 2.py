matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(0, 3):
    for c in range(0, 3):
        matriz[i][c] = int(input(f"Digite um valor para [{i}, {c}]: "))
print(str(matriz[0]).replace(" ", "][").replace(",", ""))
print(str(matriz[1]).replace(" ", "][").replace(",", ""))
print(str(matriz[2]).replace(" ", "][").replace(",", ""))