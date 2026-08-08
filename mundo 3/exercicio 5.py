lista=list()
par=list()
impar=list()
while True:
    num=int(input('Digite um numero: '))
    opçao=str(input('Quer continuar? [S/N] ')).upper()
    lista.append(num)
    if num %2==0:
        par.append(num)
    elif num %2==1:
        impar.append(num)
    if opçao == 'N':
        break
print('Os valores da listas sao:',lista)
print('Os valores pares da lista sao:',par)
print('Os valores impares da lista sao:',impar)
