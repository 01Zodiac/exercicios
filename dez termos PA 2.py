# Mostra os daz primeiros termos de uma PA (usando while)
a1 = int(input("Digite o primeiro termo da pa: "))
r = int(input("Digite a razão da pa: "))
i = 0
while i < 10:
    print(a1 + r * i, end=" ")
    i += 1
print("Fim")