nome = input('\nInsira uma frase: \n')

vezesA = nome.upper().count('A')
posipA = nome.upper().find('A')
poseuA = nome.upper().rfind('A')

print('A letra \'A\' aparece {} vezes no texto \"{}\" '.format(vezesA, nome))
print('A letra \'A\' aparece pela primeira vez na posição {}'.format(posipA))
print('A letra \'A\' aparece pela última vez na posição {}\n'.format(poseuA))