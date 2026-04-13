# Mostra os termos de uma PA de acordo com a escolha do usuário
print("Escolha a razão, o primeiro termo e quantidade de termos da PA (Digite [0] para sair do programa)\n")
op = 1
while op > 0:
    r = int(input("Razão: "))
    a1 = int(input("Primeiro termo: "))
    op = int(input("Quantidade de termos da PA para aparecer: "))
    i = 0
    while i < op:
        print(a1 + r * i, end=" ")
        i += 1
    print("Saiu do programa!") if op == 0 else print("Fim!")