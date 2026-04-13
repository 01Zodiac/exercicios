# mostra a quantidade e soma de números e sai do programa quando digitado 999

print("Digite números para no final somar e ")
num = sum = tot = 0

while num != 999:
    sum += num
    tot += 1
    num = int(input("Número ([999] para parar): "))
print("Fim!")
print(f"O total de números digitados foram {tot - 1}")
print(f"A soma dos números foi {sum}")