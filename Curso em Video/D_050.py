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
s = 0

for i in range(1, 6):
    numero = int(input('Insira o {} {}{} {} {}NÚMERO INTEIRO{}: '.format(cor['amarelof'], i, chr(176), cor['fim'], cor['amarelo'], cor['fim'])))
    if numero % 2 == 0:
        s =+ numero
final = int(input('Insira o {} ÚLTIMO {} {}NÚMERO INTEIRO{}: '.format(cor['amarelof'], cor['fim'], cor['amarelo'], cor['fim'])))

if final % 2 == 0:
    final =+ s
    print('\tA soma dos números{} PARES{} é = {}{}{}'.format(cor['vermelho'],  cor['fim'], cor['azul'], final, cor['fim']))
else:
    print('\tA soma dos números{} PARES{} é = {}{}{}'.format(cor['vermelho'],  cor['fim'], cor['azul'], s, cor['fim']))
