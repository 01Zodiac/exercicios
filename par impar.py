opc = ""
num = []
par = []
impar = []
while opc != "N":
    n = (int(input("Digite um número: ")))
    if n not in num:
        num.append(n)
        if n % 2 == 0:
            par.append(n)
        else:
            impar.append(n)
    else:
        print("Número já digitado, digite [S] para tentar novamente.")
    opc = input("Quer continuar? [S / N]: ").upper()
    if opc not in "SN":
        print("Escolha apenas entre [S] ou [N]")
        break
if opc == "N":
    print(f"Todos os números {num}")
    print(f"Todos os pares {par}")
    print(f"Todos os impares {impar}")