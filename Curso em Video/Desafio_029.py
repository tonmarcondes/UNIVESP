velocidade = eval(input('\nInforme sua velocidade: '))

delta = velocidade - 80

if velocidade <= 80:
    print('Parabéns, motorista consciente\n')
else:
    print('Você foi multado por estar {:.0f}km/h acima da velocidade permitida'.format(delta))
    print('Sua multa será de R${:.2f}\n'.format(delta * 7))
