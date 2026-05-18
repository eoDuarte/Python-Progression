from random import shuffle

n1 = input(str('Primeiro aluno: '))
n2 = input(str('Segundo aluno:'))
n3 = input(str('Terceiro aluno:'))
n4 = input(str('Quarto aluno:'))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de de apresentação é: ', lista)
