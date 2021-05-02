#Converter um numero inteiro para :
# Binário
# Hexadecimal
# octal
print('\033[1;36m------ Conversão de números ------')
num = int(input("\033[1;33mDigite um número inteiro: "))
print('''Qual a base de conversão ?
[1] para binário
[2] para hexadecimal
[3] para octal''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('\033[1;36m{} convertido para binário é igual a: {}'.format(num,bin(num)[2:]))    # [2:] O python mostra 0b na frete de todos os números binários para indicar que é um número binário essa expressão[2:] é pra printar o numero a partir do 3 caracter eliminando os 2 primeiros ( lembrando o pythin comça a contar do zero
elif opção == 2:
    print('\033[1;36m{} convertido para hexadecimal é igual a: {}:'.format(num,hex(num)[2:]))
elif opção == 3:
    print('\033[1;36m{} convertido para octal é igual a: {}'.format(num,oct(num))[2:])
else:
    opção > 3 and opção < 1
    print('\033[1;31mOpção inválida')






