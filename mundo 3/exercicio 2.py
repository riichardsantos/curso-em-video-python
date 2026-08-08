n1=int(input('Digite o primeiro numero:'))
n2=int(input('Digite o segundo numero:'))
n3=int(input('Digite o terceiro valor'))
n4=int(input('Digite o quarto valor'))
cont=0
tot=(n1,n2,n3,n4)

print('O valor nove apareceu',tot.count(9),'vezes')
if 3 in tot:
    print('O numero 3 aparece na posicao',tot.index(3))
else:
    print('o numero 3 nao foi digitado')

for n in tot:
    if n%2==0:
        print('Os numeros pares sao os valores',n)