#Define o tipo primitivo de algo digitado

a = input("digte algo: ")
print("o tipo é: ", type(a))
print("só números? ", a.isnumeric())
print("só letras? ", a.isalpha())
print("letra e número? ", a.isalnum())
print("tudo maiúsculo? ", a.isupper())
print("tudo minúsculo? ", a.islower())
print("só espaços? ", a.isspace())
print("capitalizado? ", a.istitle())
print("caracteres? ", a.isascii())