#Separa um número por unidade, dezena, centena e milhar 

numero = int(input("Digite um numero de 0 a 9999: "))
if numero < 9999:
    num = str(numero).zfill(4)
    print(f"Unidade:", (num[3]))
    print(f"Dezena:", (num[2]))
    print(f"Centena:", (num[1]))
    print(f"Milhar:", (num[0]))
else:
    print("Somente números de 0 até 9999")