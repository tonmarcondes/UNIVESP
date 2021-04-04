from math import pow
peso = eval(input('\ninforme seu \033[1;033mPESO\033[m: '))
altura = eval(input('informe sua \033[1;033mALTURA\033[m: '))

cor = {'fim':'\033[m', 'amarelo':'\033[1;033m', 'vermelho':'\033[1;031m', 'azul':'\033[1;034m', 'verde':'\033[7;32m'}

imc = peso / pow(altura, 2)

if imc < 18.5:
    print('\n{}{}{}kg: {}Abaixo do peso{}\n'.format(cor['azul'], peso, cor['fim'], cor['vermelho'], cor['fim']))
elif imc < 25:
    print('\n{}{}{}kg: {}Peso ideal{}\n'.format(cor['azul'], peso, cor['fim'], cor['vermelho'], cor['fim']))
elif imc < 30:
    print('\n{}{}{}kg: {}Sobrepeso{}\n'.format(cor['azul'], peso, cor['fim'], cor['vermelho'], cor['fim']))
elif imc < 40:
    print('\n{}{}{}kg: {}Obseidade{}\n'.format(cor['azul'], peso, cor['fim'], cor['vermelho'], cor['fim']))
else:
    print('\n{}{}{}kg: {}Obesidade mórbida{}\n'.format(cor['azul'], peso, cor['fim'], cor['vermelho'], cor['fim']))