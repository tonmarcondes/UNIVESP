bissexto = int(input('\nQue ano deseja consultar?\n\t'))

if bissexto % 4 == 0:
    print('\nO ano {} é BISSEXTO\n'.format(bissexto))
else:
    print('\nO ano {} é NÃO é BISSEXTO\n'.format(bissexto))
