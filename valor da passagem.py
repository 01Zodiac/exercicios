#Calcula o valor da passagem, se a distância percorrida for menor que 200Km é cobrado R$0.5 por Km rodado, senão, é cobrado R$0.45 por Km rodado

distancia = float(input("Imprima a distancia percorrida pelo carro: "))
if distancia < 200:
    passagem1 = (distancia * 0.5)
    print(f"O valor da passagem fica por: {passagem1}")

else:
    passagem2 = (distancia * 0.45)
    print(f"O valor da passagem fica por: {passagem2}")
