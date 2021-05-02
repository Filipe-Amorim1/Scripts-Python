#: Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.
print('\033[1;32m-=-=-=-=-= Menu de Opções =-=-=-=-=-')

operacao =  0
num1 = (int(input('\033[1;34mDigite uma número: ').strip()))
num2 = (int(input('Digite uma número: ').strip()))
while operacao != 5 :
    operacao = int(input('''Digite o operador
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa :
    Qual a sua opção:  ''').strip())
    if operacao == 1:
        print('\033[1;32m A soma entre {} e {} é igual a: {} \033[m'.format(num1,num2,num1+num2))
    elif operacao == 2:
        print('\033[1;32m A multiplicação entre {} x {} é igual a: {} \033[m'.format(num1, num2, num1*num2))
    elif operacao == 3:
        if num1 > num2:
            print('\033[1;32mO maior número é: \033[m',num1)
        if num1 < num2:
            print('1;32mO maior número é:\033[m', num2)
    elif operacao == 4:
        num1 = (int(input('Digite uma número: ').strip()))
        num2 = (int(input('Digite uma número: ').strip()))
    elif operacao == 5:
        print('Programa finalizado')
    else:
        ('Opção Inválida')