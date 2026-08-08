distancia=float(input('qual a distancia da viagem:'))
if distancia<=200:
    preço=distancia*0.50
    print('Essa viagem custará um valor de',preço,'R$')
else:
    preço=distancia*0.45
    print('Como esta viagem é mais longa, vc ganha 5 centavos de desconto')
    print('O valor é de',preço,'R$')