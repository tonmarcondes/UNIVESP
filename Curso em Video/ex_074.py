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

import random
from random import Random

brasileiro = ('Atletico-MG', 'Internacional', 'Sao Paulo', 'Flamengo', 'Palmeiras', 'Santos', 'Gremio', 'Fluminense', 'Bahia', 'Athletico-PR', 'Sport', 'Fortaleza', 'Corinthians', 'Ceara', 'Atletico-GO', 'Vasco', 'Bragantino', 'Coritiba', 'Botafogo', 'Goias')
pos = 0

titulo = "SOMA DOS NUMEROS"

print(f'{amarelo}={fim}' * 24)
print(f'{amarelof}{titulo:^24}{fim}')
print(f'{amarelo}={fim}' * 24)

