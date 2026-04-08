#Mostra se um número é primo ou não
num = int(input("Digite um número: "))
c = 0
for i in range(1, num + 1):
    if num % i == 0:
        print(f"({i})", end=" ")
        c += 1
    else:
        print(f"{i}", end=" ")
print(f"O número {num} foi divisível {c} vezes")
if c >= 2:
    print("Primo")
else:
    print("Não primo")