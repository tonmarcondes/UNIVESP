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

homemmaisvelho = ''
idademaisvelho = 0
mulheresmeno20 = 0
somatodaidades = 0
mediadasidades = 0

for i in range(1, 5):
    print('\n====== CADASTRO DA {}{} PESSOA ======'.format(i, chr(170)))
    nomes = str(input('Insira o {} NOME {}: '.format(cor['amarelo'], cor['fim']))).strip()
    idade = int(input('Insira a {} IDADE {}: '.format(cor['amarelo'], cor['fim'])))
    sexos = str(input('Insira o {} SEXO {}[M/F]: '.format(cor['amarelo'], cor['fim']))).strip()

    if sexos in 'Mm' and idade > idademaisvelho:
        idademaisvelho = idade
        homemmaisvelho = nomes

    if sexos in 'Ff' and idade < 20:
        mulheresmeno20 += 1

    somatodaidades += idade

mediadasidades = somatodaidades /4

print('\n{} é o homem mais velho com idade de {} anos'.format(homemmaisvelho.upper(), idademaisvelho))
print('A soma das idades é {}'.format(somatodaidades))
print('A média das idades é {}'.format(mediadasidades))
print('Há {} mulheres com idade abaixo de 20 anos\n'.format(mulheresmeno20))