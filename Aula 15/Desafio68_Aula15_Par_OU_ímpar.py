# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
'''from random import randint
num = 0
cpu = 0
escolha = str('')
while True:
    usu = int(input('Digite um número: '))
    escolha=str(input('Digite [ P ] para par e [ I ] para ímpar '))
    cpu = randint(1,10)
    print(f'Jogador jogou {usu} e CPU jogou {cpu}')
    jogo = usu + cpu
    if jogo % 2 == 0:
        print('PAR')
    if jogo % 2 != 0:
        print('ÍMPAR')
    if escolha in 'Pp':
        if jogo % 2 == 0:
            print('Jogador Venceu')
    if escolha in 'Ii':
        if jogo % 2 != 0:
            print('Jogador Venceu')
    else:
        print('CPU venceu')'''


from random import randint
print('Vamos jogar par ou impar:')
cp = 0
j = 0
c = 0
while True:
    cp=randint (1,10)
    j = int(input('Digite um numero: '))
    ip = int(input('[1] para PAR\n[2] para IMPAR: '))
    s=(cp+j)%2
    if ip == 1:
        if s==0:
            print(f'Voce jogou {j} e o computador {cp} e voce ganhou')
            c += 1
        if s>=1:
            break
    if ip == 2:
        if s>=1:
            print(f'Voce jogou {j} e o computador {cp} e voce ganhou')
            c += 1
        if s==0:
            break
print(f'Voce jogou {j} e o computador {cp} voce perdeu e ganhou {c} vezes seguidas')
