# Operações com dois valores com as opções: soma, multiplicação, qual é o maior, escolher novos números e sair
print("Escolha os valores e a operaçao a ser feita")
op = 0
print("Informe os valores")
n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))
while op != 5:
    op = int(input("""Operação
[1] - Somar
[2] - Multiplicar 
[3] - Maior
[4] - Novos números
[5] - Sair do programa
Escolha: """))
    if op == 1:
        print(f"A soma entre {n1} e {n2} é {n1 + n2}")
    elif op == 2:
        print(f"A multiplicação entre {n1} e {n2} é {n1 * n2}")
    elif op == 3:
        if n1 > n2:
            print(f"O maior número é {n1}")
        else:
            print(f"O maior número é {n2}")
    elif op == 4:
        print("Informe os novos valores")
        n1 = int(input("Primeiro número: "))
        n2 = int(input("Segundo número: "))
    elif op == 5:
        print("Saindo do programa...")
    else:
        print("Opção inválida. Tente novamente.")
print("Volte sempre!")