import random
print('vou pensar em um numero de 0 á 5, tente advinhar em qual eu pensei!')
n=random.randint(0,5)
num=int(input('Digite um numero de 0 a 5:'))
if num==n:
    print('ACERTOU MISERAVI')
else:
    print('ERROU, SUA TOUPEIRA,EU PENSEI EM',n)