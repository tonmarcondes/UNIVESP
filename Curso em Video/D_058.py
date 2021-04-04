import random
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

pc = 9999
tentativas = 0
vc = 0

while pc != vc:
    vc = int(input('Insira um {} NÚMERO {}[1-10]: '.format(cor['amarelo'], cor['fim'])))
    pc = random.randint(1, 10)
    tentativas += 1
print('Você realizou {}{}{} tentativas\n'.format(cor['vermelho'], tentativas, cor['fim']))