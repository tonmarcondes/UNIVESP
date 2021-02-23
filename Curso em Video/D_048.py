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

print('Soma dos números {}ÍMPARES{} de {}1{} a {}500{} divisível por 3'.format(cor['amarelo'], cor['fim'], cor['vermelho'], cor['fim'], cor['vermelho'], cor['fim']))

s = 0

for i in range(1, 501):
    if i % 2 != 0 and i % 3 == 0:
        s += i
print('\t\t    A soma é: {} {} {}'.format(cor['verdef'], s, cor['fim']))
