brasil = ('palmeiras','flamengo','fluminense','athletico-para','bragantino','bahia','coritiba','sao paulo','atletico-mineiro',
        'corinthians','cruzeiro','botafogo','vitoria','internacional','santos','gremio','vasco','remo','mirassol','chapecoense')
print('-='*30)
print('TOP 5')
for primeiros in range(0,6):
    print(brasil[primeiros])

print('-='*30)

print('5 ULTIMOS COLOCADOS')
for ultimos in range(15,20):
   print(brasil[ultimos])

print('-='*30)

print(brasil.index('chapecoense'),'É a posiçao q se encontra o chapecoense')

print('-='*30)

print('Os time em ordem alfabetica',sorted(brasil))