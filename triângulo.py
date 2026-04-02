#Define se um triângulo pode ser formado com três retas específicas

a = float(input("Digite a distância da primeira reta: "))
b = float(input("Digite a distância da segunda reta: "))
c = float(input("Digite a distância da terceira reta: "))

if a + b > c and a + c > b and b + c > a:
    print("Com essas retas é possível formar um triângulo")

else:
    print("Com essas retas não é possível formar um triângulo")
