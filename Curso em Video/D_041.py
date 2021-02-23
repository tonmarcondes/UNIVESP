import datetime
nasc = int(input('Informe seu \033[1;033mANO DE NASCIMENTO\033[m: '))

cor = {'fim':'\033[m', 'amarelo':'\033[1;033m', 'vermelho':'\033[1;031m', 'azul':'\033[1;034m', 'verde':'\033[7;32m'}

ano = datetime.date.today().year
idade = ano - nasc

if len(str(nasc)) < 4 or len(str(nasc)) > 4 or idade < 0:
    print('\nO ano de nascimento {}{}{} é {}INVÁLIDO{}, insira uma data no formato {}YYYY{}\n'.format(cor['azul'], nasc, cor['fim'], cor['vermelho'], cor['fim']))
elif idade <= 9:
    if idade == 1:
        print('\nIdade: {}{} ano{}\tCategoria: {}MIRIM{}\n'.format(cor['azul'], idade, cor['fim'], cor['vermelho'], cor['fim']))
    else:
        print('\nIdade: {}{} anos{}\tCategoria: {}MIRIM{}\n'.format(cor['azul'], idade, cor['fim'], cor['vermelho'], cor['fim']))
elif idade <= 14:
    print('\nIdade: {}{} anos{}\tCategoria: {}INFANTIL{}\n'.format(cor['azul'], idade, cor['fim'], cor['vermelho'], cor['fim']))
elif idade <= 19:
    print('\nIdade: {}{} anos{}\tCategoria: {}JÚNIOR{}\n'.format(cor['azul'], idade, cor['fim'], cor['vermelho'], cor['fim']))
elif idade == 20:
    print('\nIdade: {}{} anos{}\tCategoria: {}MASTER{}\n'.format(cor['azul'], idade, cor['fim'], cor['vermelho'], cor['fim']))
else:
    print('\nIdade: {}{} anos{}\tCategoria: {}SÊNIOR{}\n'.format(cor['azul'], idade, cor['fim'], cor['vermelho'], cor['fim']))