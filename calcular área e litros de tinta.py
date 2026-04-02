#Calcula a quantidade de litros de tinta vai usar para pintar uma párede em relação a área
#(cada metro quadrado é utilizado dois litros de tinta)

largura = float(input("Digite a largura da parede em metros: "))
altura = float(input("Digite a altura da parede em metros: "))
area = largura * altura
lit_tinta = area / 2
print(f"a área da parede é {area} e vai ser necessário {lit_tinta} litros de tinta para pintar esta parede")
