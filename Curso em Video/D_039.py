import datetime
nasc = int(input('Insira seu \033[1;033mano de nascimento\033[m: '))

cor = {'fim':'\033[m', 'amarelo':'\033[1;033m', 'vermelho':'\033[1;031m', 'azul':'\033[1;034m'}

data = datetime.date.today()
ano = data.year
idade = ano - nasc

if idade == 18:
    print('\n{}Aliste-se imediatamente{} pois você tem {}{}{} anos\n'.format(cor['vermelho'], cor['fim'], cor['azul'], idade, cor['fim']))
elif idade < 18:

    if 18 - idade > 1:
        print('\nAinda restam {}{}{} anos {}para seu alistamento{}\n'.format(cor['azul'], 18 - idade, cor['fim'], cor['vermelho'], cor['fim']))
    else:
        print('\nAinda resta {}{}{} ano {}para seu alistamento\n{}\n'.format(cor['azul'], 18 - idade, cor['fim'], cor['vermelho'], cor['fim']))
else:

    if idade - 18 > 1:
        print('\nSeu {}período de alistamento passou{} por {}{}{} anos\n'.format(cor['vermelho'] ,cor['fim'] , cor['azul'], idade - 18, cor['fim']))
    else:
        print('\nSeu {}período de alistamento passou{} por {}{}{} ano\n'.format(cor['vermelho'] ,cor['fim'] , cor['azul'], idade - 18, cor['fim']))
    