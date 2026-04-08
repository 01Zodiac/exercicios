#Mostra se uma frase é ou não um palíndromo
fr = str(input("Digite uma frase: ")).strip().upper().replace(" ", "")
inv = fr[::-1]
print(f"Frase invertida {inv}")
print(f"Você digitou {fr}")
if inv == fr:
    print("\nSua frase é um palíndromo")
else:
    print("Sua frase não é um palíndromo")