#Crie um programa que gerencie o aproveitamento de um jogador de futebol.
#  programa vai ler o nome do jogador e quantas partidas ele jogou.
#  Depois vai ler a quantidade de gols feitos em cada partida.
#  No final, tudo isso será guardado em um dicionário
#  incluindo o total de gols feitos durante o campeonato.

print('\033[1;33m-='*10,'ESTATÍSTICAS DO JOGADOR','=-\033[M'*10 )

dados ={'Nome':'','Gols':[],'Total de gols':''}

nome = str(input('Nome do jogador: '))
partidas = int(input('Número de partidas: '))
totalgols = int(0)
golspart = []
for c in range (partidas):
    gols = int(input(f'Quantos gols na partida {c+1}: '))
    golspart.append(gols)
    totalgols += gols

dados['Nome'] = nome
dados['Gols'] = golspart
dados ['Total de gols'] = totalgols
print('-='*30)
print(dados)
print('-='*30)

for k,v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {nome} jogou {partidas} partidas.')
for c,v in enumerate(golspart):
    print(f' => Na partida {c+1}, fez {v} gols.')
print(f'Foi um total de {totalgols} gols.')
print(f'Uma média de {totalgols/partidas} gols por partidas')


'''
# OUTRO JEITO DE FAZER

print('\033[1;33m-='*10,'ESTATÍSTICAS DO JOGADOR','=-\033[M'*10 )

jogador = {}
partida = []
jogador['nome'] = str(input('Nome do jogador: '))
total= int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

for c in range(0,total):
    partida.append(int(input(f'Quantos gols na partida {c}')))

jogador['gols'] = partida[:]
jogador['total'] = sum(partida)
print("-="*30)
print(jogador)

for k , v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas. ')

for i , v in enumerate(jogador['gols']):
    print(f'    > Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
'''

