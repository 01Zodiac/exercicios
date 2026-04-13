# Mostra a média, o maior e o menor de uma quantidade indeterminada de números

op = "S"
som = 0
i = 1
maior = i
menor = i
while op == "S":
    if i == 1:
        num = int(input("Digite um número: "))
        som += num
        maior = menor = num
    i += 1
    num = int(input("Digite outro número: "))
    op = input("Quer continuar? [S / N]: ").upper()
    som += num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
if op != "N":
    print("Escolha uma opção válida")
else:
    print(f"O maior número é {maior}. O menor número é {menor}")
    media = som / i
    print(f"A média dos números é {media}")
    