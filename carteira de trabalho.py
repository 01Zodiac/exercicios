from datetime import datetime
dado = dict()
dado["nome"] = input("Nome: ")
dado["idade"] = datetime.now().year - (int(input("Ano de Nascimento: ")))
dado["ctps"] = int(input("Carteira de Trabalho (0 não tem): "))
if dado["ctps"] != 0:
    dado["contratação"] = int(input("Ano de Contratação: "))
    dado["salário"] = float(input("Salário: "))
    dado["aposentadoria"] = dado["idade"] + ((dado["contratação"] + 35) - datetime.now().year)
for k, v in dado.items():
    print(f"   - {k} tem o valor {v}")