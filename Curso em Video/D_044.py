cor = {
    'fim':'\033[m', 
    'amarelo':'\033[1;033m', 
    'vermelho':'\033[1;031m', 
    'vermelhof':'\033[7;031m', 
    'azul':'\033[1;034m', 
    'verde':'\033[1;32m', 
    'verdef':'\033[7;32m', 
    'branco':'\033[1;030m'
    }

preco = float(input('\ninforme o \033[1;033mVALOR\033[m do produto: '))
print('''
Escolha uma \033[1;033mFORMA DE PAGAMENTO\033[m: 
\t {}1{} {}à   vista  - dinheiro/cheque{}: {}10%{} de desconto
\t {}2{} {}à   vista  - cartão  crédito{}:  {}5%{} de desconto
\t {}3{} {}em até  2x - cartão  crédito{}: sem desconto
\t {}4{} {}3x ou mais - dinheiro/cheque{}: {}20%{} de juros'''
.format(
   cor['vermelho'], cor['fim'], cor['branco'], cor['fim'], cor['azul'], cor['fim'],
   cor['vermelho'], cor['fim'], cor['branco'], cor['fim'], cor['azul'], cor['fim'],
   cor['vermelho'], cor['fim'], cor['branco'], cor['fim'],
   cor['vermelho'], cor['fim'], cor['branco'], cor['fim'], cor['azul'], cor['fim']
))
escolha = int(input('\t '))

if escolha < 1 or escolha > 4:
    print('\n\t\t{}ESCOLHA UM VALOR VÁLIDO{}\n'.format(cor['vermelho'], cor['fim']))
elif escolha == 1:
    print('\nDesconto {}10%{} - Total a pagar {} R${:.2f} {}\n'.format(cor['azul'], cor['fim'], cor['vermelhof'], preco * 0.9, cor['fim']))
elif escolha == 2:
    print('\nDesconto {}5%{} - Total a pagar {} R${:.2f} {}\n'.format(cor['azul'], cor['fim'], cor['vermelhof'], preco * 0.95, cor['fim']))
elif escolha == 3:
    print('\nTotal a pagar {} R${:.2f} {}\n'.format(cor['vermelhof'], preco, cor['fim']))
else:
    print('\nJuros de {}20%{} - Total a pagar {} R${:.2f} {}\n'.format(cor['azul'], cor['fim'], cor['vermelhof'], preco * 1.2, cor['fim']))



