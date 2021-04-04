n1 = float(input('Insira a nota da\033[1;033m PRIMEIRA\033[m prova: '))
n2 = float(input('Insira a nota da\033[1;033m  SEGUNDA\033[m prova: '))

cor = {'fim':'\033[m', 'amarelo':'\033[1;033m', 'vermelho':'\033[1;031m', 'azul':'\033[1;034m', 'verde':'\033[7;32m'}

media = (n1 + n2) / 2

if media < 5:
    print('\nSua média foi {}{:.1f}{} por tanto está {}REPROVADO!{}\n'.format(cor['azul'], media, cor['fim'], cor['vermelho'], cor['fim']))
elif media >= 5 and media < 7:
    print('\nSua média foi {}{:.1f}{} por tanto está {}EM RECUPERAÇÃO!{}\n'.format(cor['azul'], media, cor['fim'], cor['vermelho'], cor['fim']))
else:
    print('\nSua média foi {}{:.1f}{} por tanto está {}APROVADO!{}'.format(cor['azul'], media, cor['fim'], cor['vermelho'], cor['fim']))
    print('\t\t{}  PARABÉNS  {}\n'.format(cor['verde'], cor['fim']))
