# Calcula a tabuada de qualquer número(positivo)

print(">>>>Tabuada<<<<\n")
while True:
    num = int(input("Digite um número: "))
    if num > 0:
        print(f"Tabuada de {num}:")
        for i in range(1, 11):
            print(f"{num} x {i} = {num * i}")  
    else:
       break
print("Digite um número maior que 0")