#Calcula a soma de todos os números ímpares de 0 a 500 múltiplos de 3

soma = 0
for i in range(0, 500, 3):
    if i % 2 == 1:
        soma += i
print(f"A soma dos números ímpares de 0 a 500 múltiplos de 3 é: {soma}")
