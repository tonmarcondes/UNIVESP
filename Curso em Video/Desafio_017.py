from math import sqrt, pow
a = eval(input('Informe o valor do cateto A: '))
b = eval(input('Informe o valor do cateto B: '))
c = sqrt(pow(a, 2) + pow(b, 2))
print('A hipotenusa dos catetos A={} e B={} é {}'.format(a, b, c))