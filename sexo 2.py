sexo = ""
while sexo != "m" and sexo != "f":
    sexo = input("Digite seu sexo: ").lower()
    if sexo != "m" and sexo != "f":
        print("Escolha apenas [m / f]")
    else:
        if sexo == "m":
            print("Sexo masculino")
        else:
            print("Sexo feminino")