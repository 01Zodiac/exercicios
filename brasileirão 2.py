times = ("Flamengo", "Palmeiras", "São Paulo", "Fluminense", "Bahia",
         "Athletico-PR", "Coritiba", "Atlético-MG", "Bragantino", "Vitória",
         "Botafogo", "Grêmio", "Vasco", "Internacional", "Santos",
         "Corinthians", "Cruzeiro", "Remo", "Chapecoense", "Mirasol")
print("Tabela do brasileirão atualizada:")
print("\nPrimeiros 5:")
for i in range(0, 5):
    print(f"{i + 1} - {times[i]}")
print("\nÚltimos 4:")
for i in range(16, 20):
    print(f"{i + 1} - {times[i]}")
print("\nTimes em ordem alfabetica:")
for i in sorted(times):
    print(i)
print("\nPosição do Chapecoense:")
for i in range(0, 20):
    chape = (times[i])
    if chape == "Chapecoense":
        print(f"\nChapecoense na {i + 1} pos")