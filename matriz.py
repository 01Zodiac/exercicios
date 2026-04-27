matriz = []
d = 0
u = 0
for i in range(0, 9):
    matriz.insert(i, int(input(f"Digite um valor para [{d}, {u}]: ")))
    u += 1
    if i == 2:
        u = 0
        d += 1
    if i == 5:
        u = 0
        d += 1
print(f"[ {matriz[0]:^5} ] [ {matriz[1]:^5} ] [ {matriz[2]:^5} ]")
print(f"[ {matriz[3]:^5} ] [ {matriz[4]:^5} ] [ {matriz[5]:^5} ]")
print(f"[ {matriz[6]:^5} ] [ {matriz[7]:^5} ] [ {matriz[8]:^5} ]")

