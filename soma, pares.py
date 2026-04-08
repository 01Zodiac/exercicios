#De seis números mostra a soma de todos os pares digitados
s = 0
c = 0
for i in range(1, 7):
  n = int(input("Digite um número: "))
  if n % 2 == 0:
    s += n
    c += 1 
print(f"Você informou {c} números e a soma dos números digitados (pares) é: {s}")