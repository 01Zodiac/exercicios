def fatorial(numero, show=False):
    multi = 1
    for i in range(1, numero + 1):
        if show:
            print(i, end="")
            if i != numero:
                print(" x ", end="")
            else:
                print(f" = ", end="")
        multi *= i
    return multi
num = int(input("Número: "))
while True:
    val = input("Todos os números(True) ou só o resultado(False)? [T/F]: ").upper()
    if val == "T":
        val = True
        break
    elif val == "F":
        val = False
        break
    else:
        print("Escolha inválida")
print(fatorial(num, show=val))