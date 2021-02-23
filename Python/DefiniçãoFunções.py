altura = input('Insira sua altura em cm:\n')
sex = input('Informe h para homens e m para mulheres\n')

altura = eval(altura)

if sex == 'h':
    peso = (72.7 * altura) - 58
    print('\033[1;37mO peso ideal é: \033[7;32m', peso, '\033[0m')
elif sex == 'm':
    peso = (62.1 * altura) - 44.7
    print('\033[1;37mO peso ideal é: \033[7;32m', peso, '\033[0m')
else:
    print('\033[1;42mVc é assexuado\033[0m')
