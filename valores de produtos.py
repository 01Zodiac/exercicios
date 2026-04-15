som = mil = menor = cont = 0
barato = ""
while True:
    prod = input("Digite o nome do produto: ")
    val = float(input("Digite o valor do produto R$"))
    cont += 1
    if cont == 1 or val < menor:
        menor = val
        barato = prod
    som += val
    if val >= 1000:
        mil += 1
    op = input("Quer continuar?[S / N]: ").upper()
    if op == "S":
        continue
    elif op == "N":
        break
    else:
        print("Opção inválida")
        break
print(f"O valor total da compra foi R${som}")
print(f"a quantidade de produtos que custa mais de mil é {mil}")
print(f"O nome do produto mais barato é {barato}, e custa R${menor}")