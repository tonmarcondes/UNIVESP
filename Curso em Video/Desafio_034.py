salario = eval(input('\ninforme seu salário\n'))

if salario > 1250:
    print('Parabéns, seu novo salário é de R${:.2f}\n'.format(salario * 1.1))
else:
    print('Parabéns, seu novo salário é de R${:.2f}\n'.format(salario * 1.15))