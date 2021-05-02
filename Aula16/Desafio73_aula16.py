#: Crie uma tupla preenchida com os 20 primeiros colocados da
# Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

classificação = ('Palmeiras','Flamengo','Internacional','Grêmio','São Paulo','Atlético-MG','Athletico-PR','Cruzeiro','Botafogo','Santos','Bahia'
,'Fluminense','Corinthians','Chapecoense','Ceará','Vasco','Sport','América-MG','Vitória','Paraná')

print(classificação[:5]) # mostrar os 5 primeiros
print(classificação[-4:]) # ùltimos 4 colocados
print(sorted(classificação))
print(f'A chapecoense esta na {classificação.index("Chapecoense")+1}º posição') # colocar mais 1 pq vai começar a contar so zero , colocar aspas dupla para dar certo aspas simples iria confundir a interpolação
cont = 1
print('='*60)
print( ' Os cinco primeiros colocados')
print('')
for c in classificação[:5]:
    print(f'{cont}º {c}')  # mostrar de forma organizada a lista com a posisão contada pelo contador
    cont = cont + 1
print('='*60)
cont = 17 # aqui colocamos o contador começando do 16 / poderiamos criar uma nova var de contagem com outro nome
print('Os quatro últimos colocados ')
print('') # dar um espaço
for c in classificação[-4:]:

    print(f'{cont}º {c}')  # mostrar de forma organizada a lista com a posisão contada pelo contador
    cont = cont + 1

print('='*60)
print('Ordem alfabética')
print('')

for c in sorted(classificação):
    print(f' {c}')

