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

primeiro = int(input('\nInsira o{} PRIMEIRO TERMO{} da {}PA{}: '.format(cor['vermelho'], cor['fim'], cor['amarelo'], cor['fim'])))
razao = int(input('Insira a{} RAZÃO {} da {}PA{}: '.format(cor['vermelho'], cor['fim'], cor['amarelo'], cor['fim'])))
termos = int(10)
an = primeiro + (termos - 1) * razao # Termo Geral da PA

for i in range(primeiro, an + 1, razao):
    print('\t\t{}{}{}'.format(cor['azul'], i, cor['fim']))
