
a = eval(input('\ninforme o valor da reta \033[1;033mA\033[m: '))
b = eval(input('\ninforme o valor da reta \033[1;033mB\033[m: '))
c = eval(input('\ninforme o valor da reta \033[1;033mC\033[m: '))

cor = {'fim':'\033[m', 'amarelo':'\033[1;033m', 'vermelho':'\033[1;031m', 'azul':'\033[1;034m', 'verde':'\033[7;32m'}

if a + b > c and a + c > b and b + c > a or a == b != c or a == c != b or b == c != a:
    print('\nAs retas {}A{}, {}B{} e {}C{} formaram um triângulo'.format(cor['amarelo'], cor['fim'],cor['amarelo'], cor['fim'],cor['amarelo'], cor['fim']))
    if a == b == c:
        print('\t\t{}EQUILÁTERO{}\n'.format(cor['verde'], cor['fim']))
    elif a == b != c or a == c != b or b == c != a:
        print('\t\t{}ISÓCELES{}\n'.format(cor['verde'], cor['fim']))
    else:
        print('\t\t{}ESCALENO{}\n'.format(cor['verde'], cor['fim']))
else:
    print('\nAs retas {}A{}, {}B{} e {}C{} \033[0;31mNÃO\033[m podem formar um triângulo\n'.format(cor['amarelo'], cor['fim'],cor['amarelo'], cor['fim'],cor['amarelo'], cor['fim']))