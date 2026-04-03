#Cálculo do Índice de Massa Corporal (IMC)

alt = float(input("Digite a altura em metros: "))
peso = float(input("Digite o peso em kg: "))
imc = peso / (alt ** 2)

print("O seu IMC é: {:.2f}".format(imc))

if imc < 18.5:
    print("Classificação: Abaixo do peso")
elif imc < 25:
    print("Classificação: Peso ideal")
elif imc < 30: 
    print("Classificação: Sobrepeso")
elif imc < 40: 
    print("Classificação: Obesidade")
else: 
    print("Classificação: Obesidade mórbida")