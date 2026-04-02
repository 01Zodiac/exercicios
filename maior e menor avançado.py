# Define qual número entre três é maior ou menor

num1 = float(input("Digite o primeiro valor: "))
num2 = float(input("Digite o segundo valor: "))
num3 = float(input("Digite o terceiro valor: "))

menor = min(num1, num2, num3)
maior = max(num1, num2, num3)

print(f"O menor valor é: {menor}")
print(f"O maior valor é: {maior}")
