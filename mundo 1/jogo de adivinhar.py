import random
from colorama import init,Fore
init(autoreset=True)
print(Fore.LIGHTGREEN_EX+'Vou pensar em um numero entre 0 e 10, tente adivinhar, se for capaz HAHA')
pc=random.randint(0,10)
jogador=int(input('Diga um numero entre 0 a 10:'))
cont=0
while jogador!=pc:
    print(Fore.RED + 'VOCE ERROU HAHA', 'tente novamente')
    cont+=1
    if pc < jogador:
        jogador = int(input('Um pouco menos, Diga outro numero entre 0 a 10:'))
    elif pc > jogador:
        jogador = int(input('Um pouco mais, Diga outro numero entre 0 a 10:'))

print(Fore.LIGHTGREEN_EX+'VOCE ACERTOU, E PRECISOU DE',cont,'TENTATIVAS')