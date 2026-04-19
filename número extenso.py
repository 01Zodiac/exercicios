#Mostra o número por extenso

cont = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete",
        "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze",
        "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")
while True:
    num = int(input("Digite um número entre 0 e 20: "))
    if 20 >= num >= 0:
        break  
    print("Escolha um número válido.")
print(cont[num])
