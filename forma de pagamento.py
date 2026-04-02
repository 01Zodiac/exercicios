#Faça um programa que leia o preço de um produto e informe o preço com desconto de 10% para pagamento à vista em dinheiro ou cheque e 5% para pagamento à vista no cartão.
# Para pagamento em 2 vezes no cartão, o preço não tem desconto e para pagamento em 3 vezes ou mais no cartão, o preço tem juros de 20%.

val = float(input("Digite o valor do produto: "))
print("Digite a condição de pagamento (cartão ou cheque/dinheiro)")
pag = input("Digite 2 para cartão\nDigite 1 para cheque/dinheiro\n--> ")

if pag == "1":
    print(f"O valor fica por R${val * 0.9} com 10 por cento de desconto")
elif pag == "2":
    vez = int(input("Quantas vezes no cartão? "))
    if vez == 1:
        print(f"O valor fica por R${val * 0.95} a vista com 5 por cento de desconto")
    elif vez == 2:
        print(f"O valor fica por R${val} em 2 vezes de R${val / vez} sem juros")
    elif vez < 1:
        print("Digite um número válido")
    else:
        tot = val + (val * 0.2)
        print(f"O valor fica por R${tot} em {vez}x de R${tot / vez} com 20 por cento de juros")
else:
    print("Digite 1 ou 2")
