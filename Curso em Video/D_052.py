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

primo = int(input('\nInsira um{} NÙMERO INTEIRO {}: '.format(cor['amarelo'], cor['fim'])))
if primo < 2:
    print('\t{} NÃO É PRIMO {}'.format(cor['vermelhof'], cor['fim']))
elif primo / 2 == 1:
    print('\t{} É PRIMO {}'.format(cor['verdef'], cor['fim']))
elif primo / 1 == primo and primo / primo == 1 and primo % 2 != 0:
    print('\t{} É PRIMO {}'.format(cor['verdef'], cor['fim']))
else:
    print('\t{} NÃO É PRIMO {}'.format(cor['vermelhof'], cor['fim']))
