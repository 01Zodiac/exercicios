# Define se um triângulo pode ser formado com três retas específicas
# Além disso, define se ele é equilátero, isóceles ou escaleno

a = float(input("Digite a distância da primeira reta: "))
b = float(input("Digite a distância da segunda reta: "))
c = float(input("Digite a distância da terceira reta: "))

if a + b > c and a + c > b and b + c > a:
    print("Com essas retas é possível formar um triângulo")
    if a == b == c:
        print("É um triângulo equilátero")
    elif a == b or a == c or b == c:
        print("É um triângulo isóceles")
    elif a != b != c:
        print("É um triângulo escaleno")
else:
    print("Com essas retas não é possível formar um triângulo")
