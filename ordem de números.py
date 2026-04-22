# Mostra todos os números digitados em ordem crescente, sem repetir nenhum valor.

opc = ""
num = []
while opc != "N":
    n = (int(input("Digite um número: ")))
    if n not in num:
        num.append(n)
    else:
        print("Número já digitado, digite [S] para tentar novamente.")
    opc = input("Quer continuar? [S / N]: ").upper()
    if opc not in "SN":
        print("Escolha apenas entre [S] ou [N]")
        break
if opc == "N":
    print(f"Todos os números em ordem {sorted(num)}")
    