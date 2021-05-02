# Ler três números e falar o maior

n1 = int(input('Digite o primeiro número:').strip())
n2 = int(input('Difite o segundo número:').strip())
n3 = int(input('Digite o terceiro número:').strip())

if n1 > n2 and n1 > n3:
    print("O maior número é ",n1)
if n2 > n1 and n2 > n3:
    print('O maior número é',n2)
if n3 > n1 and n3 > n2:
    print("O maior número é",n3)
if n1 == n2 == n3:
    print('Os números são iguais')

