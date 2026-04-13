# Mostra o enésimo termo de uma sequência de fibonacci

print("Escolha a quantidade de termos de uma sequência de fibonacci (números naturais)\n")
num = int(input("Quantidade de termos: "))
raiz_5 = 5**0.5
phi = (1 + raiz_5) / 2
psi = (1 - raiz_5) / 2
f = (phi**num - psi**num) / raiz_5
print(round(f))