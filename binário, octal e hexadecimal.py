num = int(input("Digite um número qualquer: "))
print("Escolha a base de conversão (binário, octal, hexadecimal)")
con = input("Digite [1] para (binário)\nDigite [2] para (octal)\nDigite [3] para (hexadecimal)\n Sua escolha: ")

if con == "1":
    print(f"O número {num} em binário é: {bin(num)[2:]}")
elif con == "2":
    print(f"O número {num} em octal é: {oct(num)[2:]}")
elif con == "3":
    print(f"O número {num} em hexadecimal é: {hex(num)[2:].upper()}")
else:
    print("Escolha entre 1, 2 ou 3")
