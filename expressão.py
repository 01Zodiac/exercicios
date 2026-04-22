expressao = input("Digite uma expressão: ")
um = expressao.count("(")
dois = expressao.count(")")
if um == dois:
    print("Expressão válida.")
else:
    print("Expressão inválida, os parênteses não se fecham.")