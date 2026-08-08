from colorama import init, Fore
num=int(input('Digite um numero'))
tot=0

for c in range(1,num+1):
    if num%c==0:
      print(Fore.LIGHTGREEN_EX,end=' ')
      tot+=1
      init(autoreset=True)
    else:
     print(Fore.RED,end=' ')
    print(c,end=' ')
print('O número',num,'foi divisivel',tot,'vezes')
if tot ==2:
    print('Por isso ele é primo')
else:
    print('Por isso ele NAO é primo')
