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

while True:
    print(f'{amarelo}------------------------{fim}')
    n = int(input(f'Quero ver a {amarelo}TABUADA{fim} do: '))
    print(f'{amarelo}------------------------{fim}')
    if n <= 0:
        break
    for i in range(1, 11):
        print(f'{vermelho}{i}{fim} x {vermelho}{n}{fim} = {n * i}')
print(f'Programa {vermelho}TABUADA{fim} encerrado. {azul}VOLTE SEMPRE!{fim}')