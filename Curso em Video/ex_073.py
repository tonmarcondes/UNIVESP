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


brasileiro = ('Atletico-MG', 'Internacional', 'Sao Paulo', 'Flamengo', 'Palmeiras', 'Santos', 'Gremio', 'Fluminense', 'Bahia', 'Athletico-PR', 'Sport', 'Fortaleza', 'Corinthians', 'Ceara', 'Atletico-GO', 'Vasco', 'Bragantino', 'Coritiba', 'Botafogo', 'Goias')
pos = 0

print(f'{verde}={fim}' * 23)
print(f' {amarelo}CAMPEONATO BRASILEIRO{fim}')
print(f'{verde}={fim}' * 23)

escolha = 'x'

while escolha not in 'AaBbCcDd':
    print('\nEscolha uma das opções abaixo:')
    print(f'''
        {azul}A){fim} Apenas os {vermelho}5 primeiros{fim} colocados.
        {azul}B){fim} Os {vermelho}últimos 4{fim} colocados.
        {azul}C){fim} Uma lista com os times em {vermelho}ordem alfabética{fim}.
        {azul}D){fim} Em que {vermelho}posição{fim} na tabela está o time {azul}SPFC{fim}.
    ''')
    escolha = input('Digite sua escolha: ')

if escolha in 'aA':
    for i in range(5):
        print(f' {branco}{brasileiro[i]}{fim}')
elif escolha in 'bB':
    for i in range(1, 5):
        print(f' {branco}{brasileiro[-i]}{fim}')
elif escolha in 'cC':
    for times in sorted(brasileiro):
        print(f' {branco}{times}{fim}')
else:
    print(f' {branco}O São Paulo encontra-se na {brasileiro.index("Sao Paulo") + 1} posição{fim}')