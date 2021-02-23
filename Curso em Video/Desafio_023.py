numero = input('\nInsira um numero de 0 a 9999: \n')

if not numero.isnumeric():
    print('Condição inválida, insira apenas números\n')
elif len(numero) == 1:
    print('\nA unidade do número {} é {}\n'.format(numero, numero[-1]))
elif len(numero) == 2:
    print('\nA unidade do número {} é {}'.format(numero, numero[-1]))
    print('A dezena do número  {} é {}\n'.format(numero, numero[-2]))
elif len(numero) == 3:
    print('\nA unidade do número {} é {}'.format(numero, numero[-1]))
    print('A dezena do número  {} é {}'.format(numero, numero[-2]))
    print('A centena do número {} é {}\n'.format(numero, numero[-3]))
elif len(numero) == 4:
    print('\nA unidade do número {} é {}'.format(numero, numero[-1]))
    print('A dezena do número  {} é {}'.format(numero, numero[-2]))
    print('A centena do número {} é {}'.format(numero, numero[-3]))
    print('A milhar do número  {} é {}\n'.format(numero, numero[-4]))
else:
    print('O valor {} não está de acordo com o permitido\n'.format(numero))
