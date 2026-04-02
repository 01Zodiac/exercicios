#Mostra o primeiro e o último nome do usuário

nome = input("Digite seu nome completo: ").strip()
n = nome.split()
print("Seu primeiro nome é", n[0])
print("Seu último nome é", n[len(n)-1])
print(len(n))