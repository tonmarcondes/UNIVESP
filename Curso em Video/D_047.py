import time
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

print('Números {}PARES{} de {}1{} a {}50{}'.format(cor['amarelo'], cor['fim'], cor['vermelho'], cor['fim'], cor['vermelho'], cor['fim']))

for i in range(1, 51):
    if i % 2 == 0:
        print('\t\t{}{}{}'.format(cor['azul'], i, cor['fim']))
print('\t    {}   FIM   {}'.format(cor['verdef'], cor['fim']))
