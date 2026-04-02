# O programa deve ler o ano de nascimento de um atleta e mostrar sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JÚNIOR
# - Até 25 anos: SÊNIOR
# - Acima de 25 anos: MASTER

num = int(input("Digite o ano de nascimento do atleta: "))

if 2006 <= num < 2007:
    print("Sênior")

elif 2007 <= num < 2012:
    print("Junior")

elif 2012 <= num < 2017:
    print("Infantil")

elif 2017 <= num < 2026:
    print("Mirim")

elif num > 2026:
    print("Nem nasceu")

else:
    print("Master")
