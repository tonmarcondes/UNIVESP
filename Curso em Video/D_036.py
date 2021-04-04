imovel = eval(input('Informe o valor da imóvel: '))
salario = eval(input('Insira seu salário: '))
prazo = eval(input('Em quantos anos deseja pagar o imóvel? '))

prestacao = imovel / prazo / 12

if prestacao > salario * 0.3:
    print('\n Empréstimo {}NEGADO{}\n'.format('\033[7;31m','\033[m' ))
else:
    print('\n Parabéns, empréstimo {}APROVADO{}\n'.format('\033[7;32m','\033[m' ))