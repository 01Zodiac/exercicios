par = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(0, 3):
    for c in range(0, 3):
        matriz[i][c] = int(input(f"Digite um valor para [{i}, {c}]: "))
        if matriz[i][c] % 2 == 0:
            par += matriz[i][c]
for i in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[i][c]:^5}]", end="")
    print()
soma = (matriz[0][2] + matriz[1][2] + matriz[2][2])

print(f"A soma dos números pares é {par}.")
print(f"A soma dos números da terceira coluna é {soma}.")
if matriz[1][0] > matriz[1][1] and matriz[1][0] > matriz[1][2]:
    maior = matriz[1][0]
elif matriz[1][1] > matriz[1][0] and matriz[1][1] > matriz[1][2]:
    maior = matriz[1][1]
else:
    maior = matriz[1][2]
print(f"O maior valor da segunda linha é {maior}.")