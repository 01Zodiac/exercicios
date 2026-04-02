#Calcula se um empréstimo é aprovado ou não, se o a prestação mensal foi 30% maior que o salário do comprador o empréstimo é negado
#, senão for maior que 30% é aprovado

casa = float(input("Digite o valor da casa: "))
salario = float(input("Digite o seu salário: "))
anos = float(input("Digite em quantos anos você pagará: "))
meses = anos * 12
valor = casa/meses

print(f"A prestação será de R${valor}")

if salario * 0.30 < valor:
    print("Empréstimo negado")
else:
    print("Empréstimo autorizado")
