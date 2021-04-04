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

total = 0
mais1000 = 0
barato = 0
maisbarato = ''
i = 0

while True:
    print(f'\n{amarelo}-=-=-=-=-=-=-=-=-=-=-={fim}')
    print(f'Loja {amarelo}SUPER BARATÃO{fim}')
    print(f'{amarelo}-=-=-=-=-=-=-=-=-=-=-={fim}')

    produto = input(f'{amarelo}NOME{fim} do produto: ').capitalize()
    
    preco = int(input(f'Preço {amarelo}R${fim}'))
   # while preco.isnumeric() == False or preco <= 0:
    #    preco = eval(input(f'Preço {amarelo}R${fim}'))

    if i == 0:
        barato = preco
        maisbarato = produto
        i += 1

    total += preco

    if preco > 1000:
        mais1000 += 1

    if preco < barato:
        barato = preco
        maisbarato = produto

    continuar = str(input(f'Quer continuar? {vermelho}[S/N]{fim} '))
    while continuar not in 'sSnN':
        continuar = str(input(f'Quer continuar? {vermelho}[S/N]{fim} '))

    if continuar in 'nN':
        print(f'======== FIM DO PROGRAMA ========')
        print(f'Total da compra foi: R${total:.2f}')
        print(f'Temos {mais1000} custando mais de R$1000,00')
        print(f'O produto mais barato foi {maisbarato} que custa R${barato:.2f}\n')
        break
 