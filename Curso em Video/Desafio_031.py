viagem = eval(input('\nQue distância pretende viajar?\n\t'))

if viagem <= 200:
    print('\nO O preço de sua passagem é de R${:.2f}\n'.format(viagem * 0.5))
else:
    print('\nO O preço de sua passagem é de R${:.2f}\n'.format(viagem * 0.45))
