import random

a = input('informe o nome do PRIMEIRO aluno(a) ')
b = input('informe o nome do SEGUNDO aluno(a) ')
c = input('informe o nome do TERCEIRO aluno(a) ')
d = input('informe o nome do QUARTO aluno(a) ')

e = [a, b, c, d]

print('O aluno escolhido para apagar a lousa é {}'.format(random.choice(e)))
