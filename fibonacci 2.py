# Mostra os primeiros termos de sequência de fibonacci de acordo com a escolha do usuário

print("Escolha a quantidade de termos de uma sequência de fibonacci (números naturais)\n")
num = int(input("Quantidade de termos: "))
t1 = 0
t2 = 1
seq = 3
if num == 1:
    print(t1)
else:
    print(t1, t2, end=" ")
    while seq <= num:
        t3 = t1 + t2
        print(t3, end=" ")
        t1 = t2
        t2 = t3
        seq += 1
print("\nFim!")
    