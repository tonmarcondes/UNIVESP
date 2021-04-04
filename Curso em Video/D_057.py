cor = {
    'fim':'\033[m', 
    'amarelo':'\033[1;033m', 
    'amarelof':'\033[7;033m', 
    'vermelho':'\033[1;031m', 
    'vermelhof':'\033[7;031m', 
    'azul':'\033[1;034m', 
    'verde':'\033[1;32m', 
    'verdef':'\033[7;32m', 
    'branco':'\033[1;030m'
    }

sexo = input('Insira o{} SEXO {}[M/F]: '.format(cor['amarelo'], cor['fim']))
while sexo not in 'MmFf':
    if sexo not in 'MmFf':
        print('O valor {}{}{} não é válido, tente novamente!\n'.format(cor['azul'], sexo.capitalize(), cor['fim']))
        sexo = input('Insira o{} SEXO {}[M/F]: '.format(cor['amarelo'], cor['fim']))
print('{}FIM{}'.format(cor['vermelho'], cor['fim']))