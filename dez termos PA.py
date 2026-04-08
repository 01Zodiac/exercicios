#Mostra os daz primeiros termos de uma PA
a1 = float(input("Digite o primeiro termo da PA: "))
r = float(input("Digite a razão da PA: "))
for i in range(0, 10):
    print(a1 + r * i)