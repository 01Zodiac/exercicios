dados = dict()
pessoas = list()
mulheres = list()
soma = 0
while True:
    dados.clear()
    dados["nome"] = input("Nome: ")
    while True:
        dados["sexo"] = input("Sexo [M/F]: ").upper()
        if dados["sexo"] == "F":
            mulheres.append(dados["nome"])
            break
        elif dados["sexo"] == "M":
            break
        else:
            print("Opção inválida")
    while True:
        dados["idade"] = int(input("Idade: "))
        if dados["idade"] < 0:
            print("Idade inválida")
        else:
            soma += dados["idade"]
            break
    pessoas.append(dados.copy())
    while True:
        opc = input("Quer continuar? [S/N]: ").upper()
        if opc in "SN":
            break
        else:
            print("Opção inválida")
    if opc == "N":
        break
print(f"A) Ao todo temos {len(pessoas)} pessoas cadastradas.")
media = soma / len(pessoas)
print(f"B) A média de idade é de {media:.1f} anos.")
print(f"C) As mulheres cadastradas foram {mulheres}.")
print(f"\nD) Lista de pessoas que estão acima da média:")
for i in range(0, len(pessoas)):
    if pessoas[i]["idade"] >= media:
        print("    -", end="")
        for entrad, said in pessoas[i].items():
            print(f" {entrad}: {said}", end=";")
        print()
print("Encerrado.")