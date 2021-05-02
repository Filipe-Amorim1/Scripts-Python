# Fazer o usuário digitar 6 números inteiros
# Somar apenas os pares

s = 0
for c in range (1,7):
    n = int(input('Digite um número: '))
    if n%2 == 0:
        s=s+n
print('A soma dos números pares digitados é:',s)
