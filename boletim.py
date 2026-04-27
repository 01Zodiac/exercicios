lista = list()
while True:
    nome = (input("Digite o nome do aluno: "))
    nota1 = (float(input("Digite a primeira nota: ")))
    nota2 = (float(input("Digite a segunda nota: ")))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])
    opc = input("Quer continuar? [S / N]: ").upper()
    if opc not in "SN":
        while True:
            opc = input("Opção inválida. Quer continuar? [S / N]: ").upper()
            if opc in "SN":
                break
    if opc == "N":
        break
print(f"{"nº":<4}{"nome":<10}{"média":<8}\n")
for i, aluno in enumerate(lista):
        print(f"{i:<4}{aluno[0]:<10}{aluno[2]:<8.1f}")
while True:
    esc = int(input("\nMostrar as notas de qual aluno? [999 interrompe]: "))
    if esc == 999:
        break
    else:
        nota1 = lista[esc][1][0]
        nota2 = lista[esc][1][1]  
        print(f"As notas de {lista[esc][0]} foram: {nota1} e {nota2}")
print("\nPrograma encerrado...")