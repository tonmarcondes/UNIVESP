from random import randint

nome = int(input('\nInsira um número de 1 a 5: '))

randomico = randint(1, 5)

if randomico == nome:
    print('Você VENCEU\n')
else:
    print('Você PERDEU\n')
