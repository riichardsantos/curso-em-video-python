palavras = ('BATERIA',
             'RELOGIO',
             'MERCADO',
             'BOLSA',
             'CONTROLE',
             'TELA',
             'SAPATO')

for palavra in palavras:
    print('Na palavra',palavra,'temos as vogais',end=' ')
    for letra in palavra:
        if letra in 'AEIOU':
         print(letra,end=' ')
    print()
    print('-'*40)