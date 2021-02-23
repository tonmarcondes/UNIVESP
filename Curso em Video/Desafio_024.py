nome = input('\nInsira sua cidade: \n')

if nome.split()[0].upper().find('SANTO') == 0:
    print('Sua cidade começa com SANTO')
else:
    print('Sua cidade não tem nada de SANTO\n')