lista = []
expressao = input("Digite uma expressão: ")
for i in expressao:
    lista.append(i)
um = lista.count("(")
dois = lista.count(")")
if um == dois:
    print("Expressão válida.")
else:
    print("Expressão inválida, os parênteses não se fecham.")