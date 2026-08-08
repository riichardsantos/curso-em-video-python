num1=float(input('Diga um numero:'))
num2=float(input('Diga outro numero:'))
print('''O que deseja fazer com ele?:
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NUMEROS
[5] SAIR DO PROGRAMA''')
opçao=0
while opçao!=5:
    opçao = int(input('SUA OPÇÃO:'))
    if opçao==1:
     print('O resultado é',num1+num2)
    if opçao==2:
     print('O resultado é',num1*num2)
    if opçao==3:
        if num1>num2:
            maior=num1
            print('O resultado é',num1)
        else:
            maior=num2
            print('O resultado é',num2)
    if opçao==4:
     num1=float(input('Diga um numero:'))
     num2=float(input('Diga outro numero:'))