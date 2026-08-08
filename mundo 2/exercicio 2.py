velocidade=int(input('Qual velocidade do carro:'))
multa=(velocidade-80)*7
if multa:
    print('voce foi multado por estar acima da velocidade e devera pagar um valor de',multa,'R$')
else:
    print('voce estava dentro do limite de velocidade')