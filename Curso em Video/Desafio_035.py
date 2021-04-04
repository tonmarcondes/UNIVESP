
a = eval(input('\ninforme o valor da reta A: '))
b = eval(input('\ninforme o valor da reta B: '))
c = eval(input('\ninforme o valor da reta C: '))

fonte = {'branco':'\033'}

if a + b < c and a + c < b and b + c < a:
    print('\nAs retas A, B e C podem formar um triângulo\n')
else:
    print('\nAs retas A, B e C \033[0;31mNÃO\033[m podem formar um triângulo\n')