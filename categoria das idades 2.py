# O programa deve ler o ano de nascimento de um atleta e mostrar sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JÚNIOR
# - Até 25 anos: SÊNIOR
# - Acima de 25 anos: MASTER
import datetime as dat
atual = dat.date.today().year
num = int(input("Digite o ano de nascimento do atleta: "))
idade = atual - num
if 20 <= idade < 26:
    print("Sênior")
elif 15 <= idade < 20:
    print("Junior")
elif 10 <= idade < 15:
    print("Infantil")
elif 0 <= idade < 10:
    print("Mirim")
elif idade > 25:
    print("Master")
else:
    print("Nem nasceu")