import datetime
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
anos = []
idade = []
atual = datetime.date.today()
ano = atual.year

maior = 0
menor = 0

for i in range(1, 8):
    nasc = int(input('Insira o {}{}{} ANO DE NASCIMENTO {}: '.format(i ,chr(176) ,cor['amarelo'], cor['fim'])))
    anos.insert(i, ano - nasc)
    if ano - nasc < 21:
        idade.insert(i, 'MENOR')
        menor += 1
    else:
        idade.insert(i, 'MAIOR')
        maior += 1

print('')
for i in range(7):
    print('Idade: {} {} {}-{} {} {}'.format(cor['azul'], anos[i], cor['fim'], cor['vermelho'], idade[i], cor['fim']))
print('{} maiores e {} menores'.format(maior, menor))