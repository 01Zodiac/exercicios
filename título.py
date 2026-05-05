def escreva(inp):
    tam = len(inp) + 6
    print("~" * tam)
    print("   " + inp)
    print("~" * tam)

frase = input("Digite algo: ")
escreva(frase)