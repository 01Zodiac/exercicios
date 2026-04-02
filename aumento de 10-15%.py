#Calcula um aumento de salário, se o salário atual for mais de R$1250 então recebe um aumento de 10%, senão, recebe um aumento de 15%

salario = float(input("Qual o seu salário? "))

if salario > 1250:
    aumento1 = salario * 1.1
    print(f"Com o aumento seu salário fica R${aumento1}")

else:
    aumento2 = salario * 1.15
    print(f"Com o aumento seu salário fica R${aumento2}")
