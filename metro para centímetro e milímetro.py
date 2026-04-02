#Transforma um valor em metro para Km, cm e mm

metro = float(input("Digite um valor em metros: "))
centimetro = metro * 100
milimetro = metro * 1000
quilometro = metro / 1000
print(f"Esse valor em centímetros dá {centimetro} em milímetros dá {milimetro} e em quilômetros dá {quilometro}")
