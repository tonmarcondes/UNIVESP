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

ns = soma = 0

while True:
    n = int(input(f'Insira um {amarelo}NÚMERO{fim}: '))
    if n == 999:
        break
    ns += 1
    soma += n
print(f'Foram digitados {vermelho}{ns}{fim} com uma soma total de {azul}{soma}{fim}')