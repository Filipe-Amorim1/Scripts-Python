inicio = int(input('O início: '))
final = int(input('Digite o final: '))
passo = int(input('Digite o passo: '))

for c in range (inicio,final+1,passo):# lembrar de botar + 1 no final para contagem em um laço ,pois o ultimo n não conta conforme visto
    print(c)
print('FIM')

for c in range(0,5): # essa estrutura fará repetir 5 x o input digite um número
    int(input('Digite um número:'))
print(Fim)# se não colocar o print com a indentação para encerrar o px passo iria contar esse acima tb

s =0
for c in range (0,5):
    n = int(input('Digite um número: '))
    s = s+n
print('O somatório dos valores foi:  {}'.format(s))

