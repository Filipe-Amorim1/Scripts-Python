#Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.
print('\033[1;31m-='*8,'JOGO DE ADIVINHAÇÂO 2.0','=-'*8,'\033[m')
from random import randint   # importou apenas a função randonizar interiros dentro da biblioteca random
cpu = int(randint(0,10))     # var que vai randonizar números entre 0 e 10
acertou = False   # Var criada para colocar no laço while
palpites =0   # contador criado para contar quantos palpites o jogasor deu , sera somado 1 após o jogador não acertar
while not acertou:    # enquanto a var acertou for diferente dela ( ou seja verdadeia True)
    print('\033[1;32mEm que número estou pensando ? entre 0 e 10 ')
    jogador=int(input('Digite um número: '))  # aqui o jogador digita o número
    palpites = palpites +1    # contador que somará mais na var palpite cada vez que o laço repetir , só vai parar de somar qnd o jodagor acertar
    if jogador == cpu:    # condição if , se o jogador for igual ao CPU a var acetoru vira verdadeira e termina o laço terminando assim o jogo
        acertou = True
    else:   # caso o contrário do if
        if jogador < cpu :    # Se o jogador digitou um número menos que o que o cpu randonizou
            print('\033[31m Mais! tente novamente.') # ele printara esta dica
        elif jogador > cpu: # Se o jogador digitar um número maior do que o Cpu randonizopu
            print('\033[31mMenos tente mais uma vez.') # ele printara enta dica
print('\033[1;35mVocê acertou')    # mensagem que será exibida quando terminar o laço , and a var acertou for True
print('Foram {} papites até acertar'.format(palpites)) # mensagem que será exibida quando terminar o laço , and a var acertou for True
