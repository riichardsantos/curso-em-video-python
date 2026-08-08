lista=list()
cont=0
while True:
    lista.append(int(input('Digite um numero:')))
    opçao=str(input('Deseja continuar? [S/N] ')).strip().upper()
    cont+=1
    if opçao != 'S' and opçao!='N':
     print('OPÇAO INVALIDA, POR FAVOR RESPONDA COM [S/N]')
    if opçao== 'N' :
          if 5 in lista:
           print('O valor 5 foi digitado na lista')
          else:
           print('O valor 5 NAO foi digitado na lista')
          lista.sort(reverse=True)
          print('A ordem decrescente dos numeros digitados', lista)
          print('Foram digitados',cont,'numeros')
          break
