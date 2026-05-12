def ficha(j, g=0):
    print(f"O jogador {j} fez {g} gol(s).")

n = str(input("Nome do jogador: ")).strip()
g = str(input("Número de gols: ")).strip()

if g.isnumeric():
    g = int(g)
else:    
    g = 0

if n == "":
    n = "<desconhecido>"

ficha(n, g)