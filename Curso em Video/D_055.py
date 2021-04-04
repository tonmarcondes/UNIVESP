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

pesos = []

for i in range(1, 6):
    peso = int(input('Insira o {}{}{} PESO {}: '.format(i ,chr(176) ,cor['amarelo'], cor['fim'])))
    pesos.insert(i, peso)

maior = max(pesos)
menor = min(pesos)
    
print('')
for i in range(5):
    print('\t{} {}kg {}'.format(cor['azul'], pesos[i], cor['fim']))
    
print('\nO maior peso foi: {}\nO menor peso foi: {}\n'.format(maior, menor))