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

resto = 0
banco = 'BANCO TON'

print(f'\n{amarelo}-=-=-=-=-=-=-=-=-=-=-=-=-=-={fim}')
print(f'{vermelho}{banco:^28}{fim}')
print(f'{amarelo}-=-=-=-=-=-=-=-=-=-=-=-=-=-={fim}')

saque = int(input(f'Que {amarelo}VALOR{fim} deseja sacar? R$'))

if saque >= 50:
    print(f'Total de {vermelho}{saque // 50}{fim} cédulas de {verde}R$50,00{fim}')
    resto = saque % 50
else:
    resto = saque

if resto >= 20 and resto < 50:
    print(f'Total de {vermelho}{resto // 20}{fim} cédulas de {verde}R$20,00{fim}')
    resto = resto % 20

if resto >= 10 and resto < 20:
    print(f'Total de {vermelho}{resto // 10}{fim} cédulas de {verde}R$10,00{fim}')
    resto = resto % 10

if resto >= 1 and resto < 10:
    print(f'Total de {vermelho}{resto // 1}{fim} cédulas de {verde}R$1,00{fim}')
 
print(f'============================')
print(f'Volte sempre ao banco {azul}TON{fim}\n')
