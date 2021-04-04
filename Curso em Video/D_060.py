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

fat = int(input('\nInsira o {} FATORIAL {}a ser encontrado: '.format(cor['amarelo'], cor['fim'])))

i = 1
fatorial = 0

while i < fat:
    if fatorial == 0:
        fatorial = fat
    fatorial = fatorial * (fat - i)
    i += 1
print('{}{}!{} é igual a {}{}{}\n'.format(cor['vermelho'], fat, cor['fim'], cor['azul'], fatorial, cor['fim']))
