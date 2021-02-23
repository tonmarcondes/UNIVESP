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

tabuada = int(input('Insira a {}TABUADA{} que deseja gerar: '.format(cor['amarelo'], cor['fim'])))

for i in range(1, 11):
    print('\t\t    {}{}{} x {}{}{} = {}{}{}'.format(cor['vermelho'], tabuada, cor['fim'], cor['vermelho'], i, cor['fim'], cor['azul'], tabuada * i, cor['fim']))
