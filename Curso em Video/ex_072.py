# Cores terminal
fim ='\033[m'
amarelo = '\033[1;033m' 
amarelof = '\033[7;033m' 
vermelho = '\033[1;031m' 
vermelhof = '\033[7;031m' 
azul = '\033[1;034m'
azulf = '\033[7;034m'
verde = '\033[1;32m' 
verdef = '\033[7;32m' 
branco = '\033[1;030m'


numero = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
extenso = ('um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
pos = 0

n = int(input(f'{amarelo}Insira o número que deseja ver:{fim} '))

while n not in numero:
    print(f'\n{vermelho}Digite um numero valido{fim}')
    n = int(input(f'{amarelo}Insira o número que deseja ver:{fim} '))

pos = numero.index(n)
print(f'\nO numero digitado foi {azul}{extenso[pos]}{fim}.\n')
