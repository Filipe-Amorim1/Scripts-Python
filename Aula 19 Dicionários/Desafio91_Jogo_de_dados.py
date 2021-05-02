# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

print('\033[1:32m======= JOGO DE DADOS =======\033[m')
from random import randint
from  time import  sleep
from operator import itemgetter

jogo ={'Jogador 1':'','Jogador 2':'','Jogador 3':'','Jogador 4':''  }
jog1 = randint(1,6)
jog2 = randint(1,6)
jog3 = randint(1,6)
jog4 = randint(1,6)

jogo['Jogador 1'] = jog1
jogo['Jogador 2'] = jog2
jogo['Jogador 3'] = jog3
jogo['Jogador 4'] = jog4
ranking = {}
print('Vamos ao Jogo !!!!')
print()
for k , v in jogo.items():
    sleep(1.5)
    if v == 1:
        print(f'{k} com {v} ponto')
    else:
        print(f'{k} com {v} pontos')
# Para colocar em ordem no dicionário importamos da biblioteca operador a função itemgetter
print('='*29)
print('\033[1:32m======= RANKING =======\033[m')

ranking = sorted(jogo.items(),key=itemgetter(1),reverse=True)
for k, v in enumerate(ranking):
    sleep(1)
    if k == 0:
        print(f'\033[1;36m{k + 1}º colocado {v[0]}\033[m')
    else:
        print(f'{k+1}º colocado {v[0]}')


