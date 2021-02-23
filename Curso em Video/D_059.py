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

n1 = int(input('Insira o 1º {} NÚMERO {}: '.format(cor['amarelo'], cor['fim'])))
n2 = int(input('Insira o 2º {} NÚMERO {}: '.format(cor['amarelo'], cor['fim'])))

soma = n1 + n2
mult = n1 * n2
escolha = 0

while escolha != 5:
    print('''
    {}\t[1]{} {}SOMAR{}
    {}\t[2]{} {}MULTIPLICAR{}
    {}\t[3]{} {}MAIOR{}
    {}\t[4]{} {}NOVOS NÚMEROS{}
    {}\t[5]{} {}SAIR{}
    '''.format(
    cor['vermelho'], cor['fim'], cor['azul'], cor['fim'], 
    cor['vermelho'], cor['fim'], cor['azul'], cor['fim'], 
    cor['vermelho'], cor['fim'], cor['azul'], cor['fim'], 
    cor['vermelho'], cor['fim'], cor['azul'], cor['fim'], 
    cor['vermelho'], cor['fim'], cor['azul'], cor['fim']
    ))
    escolha = int(input('Selecione uma das {} OPÇÕES {}[1-5]: '.format(cor['amarelo'], cor['fim'])))

    if escolha <= 0 or escolha > 5:
        print('Escolha um número válido')
    elif escolha == 1:
        print(soma)
        escolha = 5
    elif escolha == 2:
        print(mult)
        escolha = 5
    elif escolha == 3:
        if n1 > n2:
            print(n1)
        else:
            print(n2)
        escolha = 5
    elif escolha == 4:
        n1 = int(input('Insira o 1º {} NÚMERO {}: '.format(cor['amarelo'], cor['fim'])))
        n2 = int(input('Insira o 2º {} NÚMERO {}: '.format(cor['amarelo'], cor['fim'])))
 
print('\t{}   FIM   {} \n'.format(cor['verdef'], cor['fim']))