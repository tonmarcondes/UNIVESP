nome = input('Insira seu nome completo: ')
print('Maiúsculo: {}'.format(nome.upper()))
print('Minúsculo: {}'.format(nome.lower()))
print('Total de letras sem espaços: {}'.format(len(nome.replace(' ', ''))))
print('Total de letras do primeiro nome: {}\n'.format(len(nome.split()[0])))
