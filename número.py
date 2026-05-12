def leiaint(msg):
    num = input(msg)
    if num.isnumeric():
        return int(num)
    else:
        print("\033[31mERRO! Digite um número inteiro válido.\033[m") 
    return leiaint(msg)

n = leiaint("Digite um número: ")
print(f"Você acabou de digitar o número {n}")