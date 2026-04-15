# Faz um programa sacar dinheiro de acordo com o valor colocado, cédulas de: 50, 20, 10 e 1
cinc = vin = dez = um = 0
val = int(input("Digite o valor a ser sacado: "))
while True:
    if val >= 50:
        val -= 50
        cinc += 1
    elif val >= 20:
        val -= 20
        vin += 1
    elif val >= 10:
        val -= 10
        dez += 1
    elif val >= 1:
        val -= 1
        um += 1
    else:
        break
print(f"Total de cédulas de 50: {cinc}")
print(f"Total de cédulas de 20: {vin}")
print(f"Total de cédulas de 10: {dez}")
print(f"Total de cédulas de 1: {um}")