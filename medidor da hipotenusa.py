#Calcula o valor da hipotenusa de acordo com o valor dos catetos

import math

oposto = float(input("Comprimento do cateto oposto: "))
adjacente = float(input("Comprimento do cateto adjacente: "))
hipotenusa = math.sqrt(oposto**2 + adjacente**2)
print(f"O valor da hipotenusa é: {hipotenusa:.2f}\n")
