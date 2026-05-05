from time import sleep

def linha():
    print("-=" * 30)

def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    linha()
    print(f"Contagem de {i} até {f}, de {p} em {p}")
    cont = i
    if i < f:
        while cont <= f:
            sleep(0.5)
            print(f"{cont}", end=" ")
            cont += p
        print("FIM!")
    else:
         while cont >= f:
            sleep(0.5)
            print(f"{cont}", end=" ")
            cont -= p
    print("FIM!")

contador(1, 10, 1)
contador(10, 0, 2)
print("< Personalizado >")
ini = int(input("Início: "))
fim = int(input("Fim: "))
pas = int(input("Passo: "))
contador(ini, fim, pas)

