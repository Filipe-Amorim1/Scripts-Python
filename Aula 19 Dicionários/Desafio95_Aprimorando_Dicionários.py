#  Aprimore o desafio 93 para que ele funcione com vários jogadores,
#  incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

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
