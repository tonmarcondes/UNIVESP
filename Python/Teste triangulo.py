a = eval(input('Insira um valor para A\n'))
b = eval(input('Insira um valor para B\n'))
c = eval(input('Insira um valor para C\n'))

if a == b and b == c:
    print('Triangulo equilátero\n')
elif a == b or c == b or a ==c:
    print('Triangulo Isóceles\n')
else:
    print('Triangulo Escaleno\n')
