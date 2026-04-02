#Escolhe aleatoriamente um aluno entre quatro

import random

a1 = input("Primeiro aluno: ")
a2 = input("Segundo aluno: ")
a3 = input("Terceiro aluno: ")
a4 = input("Quarto aluno: ")
chamada = [a1, a2, a3, a4]
random.shuffle(chamada)
print("\nA ordem de apresentação dos alunos será: \n", chamada)
