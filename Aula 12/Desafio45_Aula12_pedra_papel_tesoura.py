# criar um programa para o jogo JOKENPÔ
# o famoso pedra,papel ou tesoura
import random
from time import sleep
itens = ('Pedra','Papel','Tesoura')
cpu = random.randint(0,2)# 3 POSSIBILIDADES     , PYTHON COMEÇA A CONTAR DO ZERO (0,1,2)

print('\033[1;32m-='*6,'JOKENPÔ','-='*6)
print('''\033[1;35mDigite 
[ 0 ] para pedra
[ 1 ] para papel
[ 2 ] para tesoura''')
jogador = int(input('\033[1;34mDigite sua escolha:  '))
if jogador > 2 or jogador < 0:
    print('\033[31mJogada Inválida,escolha um número conforme instrução de 0 até 2.\033[m')

print('JO')
sleep(1) # comando para esperar 1 segundo. No caso vai esperar um segundo para dar o px print
print('KEN')
sleep(1)
print('PO')
sleep(1)
print('-='*15)
print('O computador escolheu {}'.format(itens[cpu])) # Este comando fará com que ao invés de randonizar entre 0 até 2 sera randonizado de 0 até 2 na posição da lista da variável itens . Sendo 0 = pedra , 1 = papel , 3 = tesoura
print('Você jogou {}'.format(itens[jogador]))

if cpu == 0:
    if jogador == 0:
        print('\033[1;32mEmpate')
    elif jogador ==1:
        print('\033[1;32mVocê venceu')
    elif jogador == 2:
        print('\033[1;32mComputador venceu')

elif cpu == 1:
    if jogador == 0:
        print('\033[1;32mComputador venceu')
    elif jogador ==1:
        print('\033[1;32mEmpate')
    elif jogador == 2:
        print('\033[1;32mVocê venceu')

elif cpu == 2:
    if jogador == 0:
        print('\033[1;32mVocê venceu')
    elif jogador ==1:
        print('\033[1;32mComputador venceu')
    elif jogador == 2:
        print('\033[1;32mEmpate')

