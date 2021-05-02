# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear
# 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
'''from time import sleep
from random import randint

mega= [randint(1,60),randint(1,60),randint(1,60),randint(1,60),randint(1,60),randint(1,60)]
listaapalp =[]
cont=0
n = 0
n = int(input('Quantos palpites você quer gerar?'))
print('Aqui está a sua lista de palpites')
for c in range(n):
    palpites = [randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60)]
    listaapalp.append(palpites[:])
    sleep(1)
    cont+=1
    print(f'Jogo {cont}: {palpites}')

print('Os números sorteados foram :')
print(mega) '''
from random import sample
from time import sleep
jogos=list()
n=int(input('Quantos jogos?: '))
for c in range(n):
  a=sorted(sample(range(1, 61), 6))# gerar 6 números de 1 até 60 sem / o sorted é para por em ordem crescente
  jogos.append(a[:])
  print(f'Jogo {c+1}: {a}')
  sleep(0.5)

