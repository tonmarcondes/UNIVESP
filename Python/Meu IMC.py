#MEU IMC

peso = eval(input('Informe seu peso\n'))
alt =  eval(input('Informe sua altura\n'))
imc = (peso/alt**2)

if imc < 18.5:
    print('Você está abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('Você está com peso normal')
else:
    print('Você está acima do peso')
