nota50=50
nota20=20
nota10=10
nota1=1
cont=0
total=0
resto=0
valor=total
valor=int(input('Quanto vc deseja sacar?:'))
while valor>0:
    if valor>=50:
        nota50=valor//50
        resto=valor%50
        print('Voce receberá',nota50,'notas de 50 R$')
    if resto:
        nota20=resto//20
        resto=resto%20
        print('Voce receberá',nota20,'notas 20 R$')
    if resto>=10:
      nota10=resto//10
      resto=resto%10
      print('Voce receberá',nota10,'notas 10 R$')
    if resto>=1:
        nota1=resto//1
        resto=resto%1
        print('Voce receberá',nota1,'notas 1 R$')
    break
