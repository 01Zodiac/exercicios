def notas(*val, sit=False):
    """
    -> dict
    -> :Recebe várias notas de alunos e retorna um dicionário com várias informações sobre a situação do aluno.
    -> val: uma ou mais notas dos alunos (aceita várias)
    -> sit: valor opcional, indicando se deve ou não adicionar a situação do aluno
    -> return: dicionário com várias informações sobre a situação do aluno.
    """
    med = 0
    info = dict()
    info["total"] = len(val)
    info["maior"] = max(val)
    info["menor"] = min(val)
    for i in range(0, len(val)):
        med += val[i]
    info["média"] = med/len(val)
    if sit:
        if info["média"] > 6:
            info["situação"] = "Boa"
        else:
            info["situação"] = "Ruim"
    return info

valores = list()
while True:
    num = float(input("Digite uma nota [nota 11 para parar]: "))
    if num == 11:
        break
    elif num > 11:
        print("Nota inválida")
    else:
        valores.append(num)

while True:
    val = input("Situação? [S/N]: ").upper()
    if val == "S":
        val = True
        break
    elif val == "N":
        val = False
        break
    else:
        print("Escolha inválida")

resp = notas(*valores, sit=val)
print(resp)
help(notas)