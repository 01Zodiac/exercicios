#Mostra se uma frase é ou não um palíndromo
fr = str(input("Digite uma frase: ")).strip().upper()
p = fr.split()
junto = "".join(p)
inv = ""
for i in range(len(junto) - 1, -1, -1):
    inv += junto[i]
print(f"Frase invertida {inv}")
print(f"Você digitou {junto}")
if inv == junto:
    print("Sua frase é um palíndromo")
else:
    print("Sua frase não é um palíndromo")
