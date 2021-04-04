inteiro = int(input('Insira um número inteiro: '))
base = int(input('Digite o valor correspondente a base:\n\t \033[1;34m1\033[m para \033[1;31mbinário\033[m\n\t \033[1;34m2\033[m para \033[1;31moctal\033[m\n\t \033[1;34m3\033[m para \033[1;31mhexadecimal\033[m\n\t '))

if base < 1 or base > 3:
    print('\n\033[7;31mVALOR ILEGAL\033[m')
elif base == 1:
    print('\nO número \033[133m{}\033[m convertido para binário é \033[133m{}\033[m\n'.format(inteiro, bin(inteiro)))
elif base == 2:
    print('\nO número \033[133m{}\033[m convertido para octal é \033[133m{}\033[m\n'.format(inteiro, oct(inteiro)))
else:
    print('\nO número \033[133m{}\033[m convertido para hexadecimal é \033[133m{}\033[m\n'.format(inteiro, hex(inteiro)))
