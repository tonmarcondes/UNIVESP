# Cores terminal
fim ='\033[m'
amarelo = '\033[1;033m' 
amarelof = '\033[7;033m' 
vermelho = '\033[1;031m' 
vermelhof = '\033[7;031m' 
azul = '\033[1;034m'
verde = '\033[1;32m' 
verdef = '\033[7;32m' 
branco = '\033[1;030m'

mais18 = 0
h = 0
m20 = 0

while True:
    print(f'\n{amarelo}-=-=-=-=-=-=-=-=-=-=-={fim}')
    print(f'Cadaste uma {amarelo}PESSOA{fim}')
    print(f'{amarelo}-=-=-=-=-=-=-=-=-=-=-={fim}')

    idade = input(f'Informe a  {amarelo}IADADE{fim}: ')
    while idade.isnumeric() == False:
        idade = input(f'Informe a  {amarelo}IADADE{fim}: ')
    
    idade = int(idade)


    sexo = str(input(f'Sexo {amarelo}[H/F]{fim}: '))
    while sexo not in 'HhFf':
        sexo = str(input(f'Sexo {amarelo}[H/F]{fim}: '))


    if idade > 18:
        mais18 += 1

    if sexo in 'Hh':
        h += 1

    if sexo in 'Ff' and idade < 20:
        m20 += 1

    continuar = str(input(f'Quer continuar? {vermelho}[S/N]{fim} '))
    while continuar not in 'sSnN'
        continuar = str(input(f'Quer continuar? {vermelho}[S/N]{fim} '))

    if continuar in 'nN':
        print(f'======== FIM DO PROGRAMA ========')
        print(f'Total de pessoas com mais de 18 anos: {mais18}')
        print(f'Ao todo temos {h} homens cadastrados')
        print(f'E temos {m20} mulheres com menos de 20 anos\n')
        break
 