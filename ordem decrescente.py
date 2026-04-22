# Mostra todos os números digitados em ordem decrescente, sem repetir nenhum valor, mostra quantos números foram digitados e se o valor 5 está na lista.

i = 0
opc = ""
num = []
while opc != "N":
    i += 1
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
    num.sort(reverse=True)
    if i <= 1:
        print(f"Foi digitado {i} número")
    else:
        print(f"Foram digitados {i} números")
    print(f"Todos os números em ordem decrescente {num}")
    if 5 in num:
        print("O valor 5 está na lista")
    else:
        print("O valor 5 não está na lista")