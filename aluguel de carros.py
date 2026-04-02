#Calcula preço do aluguel de um carro específico (dia = R$60)(R$0.15 por km rodado)

tempo = float(input("Quantos dias alugados? "))
distancia = float(input("Quantos quilômetros rodados? "))
preco_tempo = tempo * 60
preco_distancia = distancia * 0.15
valor = preco_distancia + preco_tempo
print(f"O valor total a pagar é R${valor:.2f}\n")