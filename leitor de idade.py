
import datetime as dat
atual = dat.date.today().year
n = int(input(f"Digite o ano de nascimento da pessoa:"))
idade = atual - n 
print(f"A pessoa tem {idade} anos")
if idade >= 18:
    print("Essa pessoa é de maior")
else:
    print("Essa pessoa é de menor")