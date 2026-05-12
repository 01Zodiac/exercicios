from datetime import datetime
def voto(ano):
    idade = datetime.now().year - ano
    if idade >= 18:
        print(f"Com {idade} anos: VOTO OBRIGATÓRIO.")
    elif idade < 16:
        print(f"Com {idade} anos: VOTO NEGADO.")
    else:
        print(f"Com {idade} anos: VOTO OPCIONAL.")
ano = int(input("Quando você nasceu? [ano]: "))
voto(ano)