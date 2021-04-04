import random

a = str(input('informe o nome do PRIMEIRO aluno(a) '))
b = str(input('informe o nome do SEGUNDO aluno(a) '))
c = str(input('informe o nome do TERCEIRO aluno(a) '))
d = str(input('informe o nome do QUARTO aluno(a) '))
print('\n')

lista = [a, b, c, d]
random.shuffle(lista)

for i in range(4):
#i = 2
    print('{} é o {}{} aluno'.format(lista[i], i + 1, chr(176)))
    
