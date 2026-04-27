lista = []
par = []
impar = []
for i in range(1, 8):
    num = int(input(f"Digite o {i}º número: "))
    lista.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
impar.sort()
par.sort()
print(par)
print(impar)