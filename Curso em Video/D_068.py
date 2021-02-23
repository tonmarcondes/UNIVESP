import random
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

pc = random.randint(0, 10)
res = ''
vit = 0

while True:
    print(f'{amarelo}-=-=-=-=-=-=-=-=-=-=-={fim}')
    print(f'Vamos jogar {amarelo}IMPAR/PAR{fim}')
    print(f'{amarelo}-=-=-=-=-=-=-=-=-=-=-={fim}')

    n = int(input(f'Diga um  {amarelo}valor{fim}: '))
    ip = str(input(f'Informe {amarelo}[P/I]{fim}: ')).upper()

    if (pc + n) % 2 == 0:
        res = 'PAR'
    else:
        res = 'IMPAR'

    if ip == res[0]:
        print(f'----------------------------------------------')
        print(f'Você jogou {n} e o computador {pc}. Total de {pc + n} {res}')
        print(f'----------------------------------------------')
        print(f'VOCÊ VENCEU!\nVamos jogar novamente...\n')
        vit += 1
    else:
        print(f'-------------------------------------------------')
        print(f' Você jogou {n} e o computador {pc}. Total de {pc + n} {res}')
        print(f'-------------------------------------------------')
        print(f'VOCÊ PERDEU!\n{vermelho}GAME OVER!{fim} Você venceu {vit} vezes')
        break
print(type(ip), ip)
print(type(res), res)