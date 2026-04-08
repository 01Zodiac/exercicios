import datetime as dat
atual = dat.date.today().year
c = 0
for i in range(1, 8):
    n = int(input(f"Digite o ano de nascimento da pessoa {i}:"))
    idade = atual - n
    print(f"A pessoa tem {idade} anos")
    if idade >= 18:
        c += 1
        print("Essa pessoa é de maior\n")
    else:
        print("Essa pessoa é de menor\n")
print(f"No total {c} são de maior e {i - c} são de menor")
