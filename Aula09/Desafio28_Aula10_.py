# Fazer o  PC pensar em um numero inteiro entre 0 e 5
# Usuario vai tentar descobrir qual foi o número esolhido pelo PC
# O programa deverá ecrever na tela se o usuário venceu ou perdeu

import random
import emoji
ale = int(random.randint(0,5))
num = int(input('Tente adivinhar o número que estou pensando de 1 até 5:').strip()) # strip para não ter problems com o usuário dar espaços no começo
print(('-'*25))# Esses comandos são para colorir a tela , vai printar 25 vezes o traço -
if num == ale:
    print("Parabéns você acertou!!!",ale,'\nfoi exatamente o número que pensei ')
else:
    print(emoji.emojize("Você errou:punch:!!! o número que pensei foi {}".format(ale),use_aliases=True)) # coloquei algo mais para ter um emoji ( ver exercicio aula 08)
#print(emoji.EMOJI_ALIAS_UNICODE_ENGLISH) # esse coando printa todos os códigos para botar os emojis


