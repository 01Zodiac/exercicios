# Um programa que recebe 5 números e informa o maior número e a posição que ele se encontra.

num = []
for i in range(0, 5):
    num.append(int(input(f"Digite um número na posição {i}: ")))
print(f"Os números digitados foram {num}")
mai = max(num)
men = min(num)
print(f"O maior número é {mai}")
texto = ""
for i, v in enumerate(num):
    if v == mai:
        if texto == "":  
            texto = f"Posição {i}"
        else:  
            texto = texto + f", Posição {i}"
print(texto)
print(f"O menor número é {men}")
texto = ""
for i, v in enumerate(num):
    if v == men:
        if texto == "":
            texto = f"Posição {i}"
        else:
            texto = texto + f", Posição {i}"
print(texto)