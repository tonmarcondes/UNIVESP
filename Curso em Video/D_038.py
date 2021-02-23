n1 = int(input('Insira o primeiro número inteiro: '))
n2 = int(input('Insira o  segundo número inteiro: '))

cores = {'fim':'\033[m', 'vermelho':'\033[1;31m','azul':'\033[1;34m'}

if n1 > n2:
    print('\nO {}primeiro valor{} é {}maior{}\n'.format(cores['vermelho'], cores['fim'], cores['azul'], cores['fim']))
elif n1 < n2:
    print('\nO {}segundo valor{} é {}maior{}\n'.format(cores['vermelho'], cores['fim'], cores['azul'], cores['fim']))
else:
    print('\n{}Não existe{} valor maior, os dois são {}iguais{}\n'.format(cores['vermelho'], cores['fim'], cores['azul'], cores['fim']))
