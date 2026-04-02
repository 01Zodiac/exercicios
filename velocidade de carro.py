#Define se um carro foi multado (velocidade acima de 80Km/h) e calcula o valor da multa (R$7 por km/h acima do limite)

velocidade = float(input("Digite a velocidade do carro(Limite de 80km/h): "))
if velocidade > 80:
    print("O carro foi multado")
    multa = (velocidade - 80) * 7
    print(f"A multa vai custar R${multa}")
else:
    print("O carro não foi multado")
