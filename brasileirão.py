times = ("Flamengo", "Palmeiras", "São Paulo", "Fluminense", "Bahia",
         "Athletico-PR", "Coritiba", "Atlético-MG", "Bragantino", "Vitória",
         "Botafogo", "Grêmio", "Vasco", "Internacional", "Santos",
         "Corinthians", "Cruzeiro", "Remo", "Chapecoense", "Mirasol")
print(f"\n{times[0:5]}")
print(f"\n{times[16:20]}")
print(f"\n{sorted(times)}")
for i in range(0, 20):
    chape = (times[i])
    if chape == "Chapecoense":
        print(f"\nChapecoense na {i + 1} pos")