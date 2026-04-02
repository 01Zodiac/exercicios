#Defina dois números e mostre qual é o maior ou se são iguais

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

if num1 > num2:
    print("O primeiro valor é maior")
elif num1 < num2:
    print("O segundo valor é maior")
elif num1 == num2:
    print("Os dois valores são iguais")
else:
    print("erro")