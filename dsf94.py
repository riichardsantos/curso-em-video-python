from colorama import init,Fore
init(autoreset=True)
soma=cont=media=0
cont_media=0
dados=dict()
lista=list()
while True:
    dados['nome']=str(input('Nome:'))
    dados['sexo']=str(input('Sexo:'))
    while dados['sexo'] not in "FfMm":
        print(Fore.RED+'RESPOSTA INVÁLIDA', 'responda com [F ou M]')
        dados['sexo']=str(input('Sexo:'))
    dados['idade']=int(input('Idade:'))
    lista.append(dados.copy())  #SEM O ".COPY" A LISTA REPETE DOS DADOS
    soma+=dados['idade']
    cont_media+=1
    media=soma/cont_media
    if dados['sexo'] in 'Ff':
        cont += 1
    resp=str(input('Quer continuar? [S/N]'))
    while resp not in 'SsNn':
        print(Fore.RED+'RESPOSTA INVÁLIDA', 'responda com [S ou N]')
        resp=str(input('Quer continuar?'))
    if resp in 'Nn':
        print('-=' * 30)
        print('Foram cadastradas',len(lista),'pessoas')
        print('-='*30)
        print(f'A média de idades cadastradas é de {media:5.2f} anos')
        print('-='*30)
        print('Foram cadastradas',cont,'Mulheres')
        break
for p in lista:
    if p['idade']>=media:
        media=p['idade']
        print('As pessoas com idades acima da média sao:', end=' ')
        for k, v in p.items():
            print(f'{k} = {v}')