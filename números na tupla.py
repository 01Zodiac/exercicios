# Mostra os números digitados, quantas vezes o 9 apareceu, a posição do 3 e os números pares

num = ()
par = ()
noves = 0
for i in range(4):
    l = int(input("Número: "))
    num += (l,)
    if l % 2 == 0:
        par += (l,)
print(f"Os números digitados foram:{num}")
print(f"O número 9 apareceu {num.count(9)}x")
if 3 in num:
    print(f"O número 3 apareceu na posição {num.index(3)+1}ª")
if par == ():
    print("Não teve números pares")
else:
    print(f"Os números pares foram {par}")
