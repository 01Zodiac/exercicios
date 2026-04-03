#jogo de pedra, papel ou tesoura contra o computador
import random

print("<< Vamos jogar pedra, papel ou tesoura >>")
comp = random.randint(1, 3)
esc = int(input(""">> Escolha digitando o número <<
Pedra [ 1 ]
Papel [ 2 ]
Tesoura [ 3 ]
Sua escolha: """))

if esc == 1 and comp == 1:
    print("Empatou, escolhi Pedra também")
elif esc == 2 and comp == 2:
    print("Empatou, escolhi Papel também")
elif esc == 3 and comp == 3:
    print("Empatou, escolhi Tesoura também")
elif esc == 1 and comp == 2:
    print("Perdeu, escolhi Papel")
elif esc == 1 and comp == 3:
    print("Ganhou, escolhi Tesoura")
elif esc == 2 and comp == 1:
    print("Ganhou, escolhi Pedra")
elif esc == 2 and comp == 3:
    print("Perdeu, escolhi Tesoura")
elif esc == 3 and comp == 1:
    print("Perdeu, escolhi Pedra")
elif esc == 3 and comp == 2:
    print("Ganhou, escolhi Papel")
else:
    print("Escolha apenas [ 1 ], [ 2 ] ou [ 3 ]")
