from math import sin, cos, tan, radians

a = int(input('Informe o valor do angulo do triângulo: '))

print('O seno do ângulo {}{} é {:.2f}'.format(a, chr(176), sin(radians(a))))
print('O coseno do ângulo {}{} é {:.2f}'.format(a, chr(176), cos(radians(a))))
print('A tangente do ângulo {}{} é {:.2f}'.format(a, chr(176), tan(radians(a))))
