from time import sleep
def maior(* num):
    print("Analisando os valores passados...")
    for v in num:
        print(f"{v} ", end="", flush=True)
        sleep(0.3)
    maior = max(num)
    print(f"\nO maior valor informado foi {maior}")
maior(1, 2, 67, 4, 5)
maior(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)