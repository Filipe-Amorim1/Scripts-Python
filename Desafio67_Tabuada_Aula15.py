#  Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
#  O programa será interrompido quando o número solicitado for negativo.

print('\033[1;32m-='*10 ,'TABUADA 3.0','=-'*10)

while True  :  # Laço infinito
    num = int(input('Digite um número: '))  # var criada para o usuario digitar um numero
    if num <0: # if conforme o enunciado para parar o programa se op usuário digitar num menor q zero
        break
    for c in range (1,11,1): # laço da tabuada repetira um número de 1 a 10 pulando de um em um començando em 1
        print(f'{num} x {c} = {num * c}')  # print da tabuada numero dig x contador
    print('-='*30)
print('\033[1;31mPrograma encerrado')


