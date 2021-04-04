import random

cor = {
    'fim':'\033[m', 
    'amarelo':'\033[1;033m', 
    'vermelho':'\033[1;031m', 
    'vermelhof':'\033[7;031m', 
    'azul':'\033[1;034m', 
    'verde':'\033[1;32m', 
    'verdef':'\033[7;32m', 
    'branco':'\033[1;030m'
    }

print('''
Escolha uma das opções abaixo: 
\t {}1{} {}PEDRA{}:
\t {}2{} {}PAPEL{}:
\t {}3{} {}TESOURA{}:'''.format(
   cor['vermelho'], cor['fim'], cor['azul'], cor['fim'],
   cor['vermelho'], cor['fim'], cor['azul'], cor['fim'],
   cor['vermelho'], cor['fim'], cor['azul'], cor['fim']
))

eu = int(input('\t '))
if eu == 1:
    me = 'PEDRA'
elif eu == 2:
    me = 'PAPEL'
else:
    me = 'TESOURA'

pc = ['PEDRA', 'PAPEL', 'TESOURA']
random.shuffle(pc)

if eu < 1 or eu > 3:
    print('\n\t\t{}ESCOLHA UM VALOR VÁLIDO{}\n'.format(cor['vermelho'], cor['fim']))
elif eu == 1 and pc[0] == 'PEDRA' or eu == 2 and pc[0] == 'PAPEL' or eu == 3 and pc[0] == 'TESOURA':
    print('{}EU{}: {}\t\t{}PC{}: {}'.format(cor['vermelho'], cor['fim'], me, cor['vermelho'], cor['fim'], pc[0]))
    print('{} EMPATE, JOGUE OUTRA VEZ {}\n'.format(cor['vermelhof'], cor['fim']))
elif eu == 1 and pc[0] == 'PAPEL':
    print('{}EU{}: {}\t\t{}PC{}: {}'.format(cor['vermelho'], cor['fim'], me, cor['vermelho'], cor['fim'], pc[0]))
    print('PAPEL {}EMBRULHA{} PEDRA\n'.format(cor['amarelo'], cor['fim']))
elif eu == 1 and pc[0] == 'PAPEL':
    print('{}EU{}: {}\t\t{}PC{}: {}'.format(cor['vermelho'], cor['fim'], me, cor['vermelho'], cor['fim'], pc[0]))
    print('PEDRA {}QUEBRA{} TESOURA\n'.format(cor['amarelo'], cor['fim']))
elif eu == 2 and pc[0] == 'PEDRA':
    print('{}EU{}: {}\t\t{}PC{}: {}'.format(cor['vermelho'], cor['fim'], me, cor['vermelho'], cor['fim'], pc[0]))
    print('PAPEL {}EMBRULHA{} PEDRA\n'.format(cor['amarelo'], cor['fim']))
elif eu == 2 and pc[0] == 'TESOURA':
    print('{}EU{}: {}\t\t{}PC{}: {}'.format(cor['vermelho'], cor['fim'], me, cor['vermelho'], cor['fim'], pc[0]))
    print('TESOURA {}CORTA{} PAPEL\n'.format(cor['amarelo'], cor['fim']))
elif eu == 3 and pc[0] == 'PEDRA':
    print('{}EU{}: {}\t\t{}PC{}: {}'.format(cor['vermelho'], cor['fim'], me, cor['vermelho'], cor['fim'], pc[0]))
    print('PEDRA {}QUEBRA{} TESOURA\n'.format(cor['amarelo'], cor['fim']))
else:
    print('{}EU{}: {}\t\t{}PC{}: {}'.format(cor['vermelho'], cor['fim'], me, cor['vermelho'], cor['fim'], pc[0]))
    print('TESOURA {}CORTA{} PAPEL\n'.format(cor['amarelo'], cor['fim']))

