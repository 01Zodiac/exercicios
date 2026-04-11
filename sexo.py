while True:
    sexo = input("Digite seu sexo: ").lower()
    if sexo == "m":
        print("Sexo masculino")
        break
    elif sexo == "f":
        print("Sexo feminino")
        break
    else:
        print("Escolha apenas [m / f]")