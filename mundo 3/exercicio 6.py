alunos=list()
media=0
temp=0
resp2=0
cont=0
while True:
    nome=str(input('Nome do aluno:'))
    nota1=float(input('Primeira nota:'))
    nota2=float(input('Segunda nota:'))
    resp=str(input('Deseja adicionar mais alguem?[S/N]')).upper()
    media = (nota1 + nota2) / 2
    temp = ([nome,[nota1,nota2], media])
    alunos.append(temp)
    if resp in 'N':
        break
print('-='*30)
print(f'{"NÚM.":<4}{"NOME":<10}{"MÉDIA":>8}')
for i, a in enumerate(alunos):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
print('-='*30)
while resp2 != 999:
    resp2=int(input('Deseja ver a nota de qual aluno? (999) para encerrar:'))
    if resp2 <= len(alunos)-1:
        print('As notas de',alunos[resp2][0],'Sao',alunos[resp2][1])
        print('-='*30)
print('PROGRAMA FINALIZADO')