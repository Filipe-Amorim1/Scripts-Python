#Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.
print('\033[1;31m-='*8,'JOGO DE ADIVINHAÇÂO 2.0','=-'*8,'\033[m')
import random
cpu = int(random.randint(0,10))
num = int(15) # coloquei 15 poderia ser qualquer num inteiro que não estivesse entre 0 e 10 , pois se estivesse entre 0 e 10 o jogo já poderia começar com o nun q o cpu pensou
palpites =0
while num != cpu:
    print('\033[1;32mEm que número estou pensando ? entre 0 e 10 ')
    num=int(input('Digite um número: '))
    palpites = palpites +1
    if num != cpu:
        print('\033[31mVocê errou! tente novamente')
print('Você acertou')
print('Foram {} papites até acertar'.format(palpites))
