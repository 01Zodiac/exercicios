# Entre 4 pessoas, mostra: quantas mulheres com menos de 20 anos, a média da idade de todos e mostra qual é o homem mais velho e sua idade 
velho = 0
novo = 0
m20 = 0
s = 0
hnome = ""
for i in range(1, 5):
    print(f"\nPessoa {i}")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo [m] / [f]: ").lower()
    if sexo == "m" or sexo == "f":
        s += idade
        if sexo == "f" and idade < 20:
            m20 += 1
        if i == 1:
           velho = i
           novo = i
           hnome = nome
        else:
            if sexo == "m":
                if idade > velho:
                    velho = idade
                    hnome = nome
                if idade < novo:
                    novo = idade 
    else:
        print("Escolha [m] ou [f] (sem parênteses)")
media = s / 4
print(f"A quantidade de mulheres com menos de 20 anos é {m20}")
print(f"A média das idades é {media}")
print(f"A idade do homem mais velho é {velho} -{hnome}")
