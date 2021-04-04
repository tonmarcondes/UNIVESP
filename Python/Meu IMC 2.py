#MEU IMC

def imc(p,a):
    'Funcção para cálculo de IMC onde p recebe o peso e a recebe altura'
    
    if p/a**2 < 18.5:
        print('Você está abaixo do peso')
    elif p/a**2 >= 18.5 and p/a**2 < 25:
        print('Você está com peso normal')
    else:
        print('Você está acima do peso')
