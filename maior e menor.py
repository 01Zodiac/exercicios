#Define qual número entre três é maior ou menor

num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro: "))
num3 = float(input("Digite mais um: "))

if num1 < num2 < num3:
    print(f"{num3} é  o maior, {num1} é o menor")

elif num1 < num3 < num2:
    print(f"{num2} é o maior, {num1} é o menor")

elif num2 < num1 < num3:
    print(f"{num3} é o maior, {num2} é o menor")

elif num2 < num3 < num1:
    print(f"{num1} é o maior, {num2} éo menor")

elif num3 < num2 < num1:
    print(f"{num1} é o maior,{num3} é o menor")

else:
    print(f"n{num2} é o maior, {num3} é o menor")
