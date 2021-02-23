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

palindromo = input('\nInsira uma{} FRASE {}: '.format(cor['amarelo'], cor['fim']))
palindromo = palindromo.split()

reverso = list(palindromo)
reverso.reverse()
reverso = ''.join(reverso)

if palindromo.lower() == reverso.lower():
    print('\t{} {} É PALíNDROMO {}\n'.format(palindromo ,cor['verdef'], cor['fim']))
else:
    print('\t{} {} NÃO É PALÍNDROMO {}\n'.format(palindromo ,cor['vermelhof'], cor['fim']))
