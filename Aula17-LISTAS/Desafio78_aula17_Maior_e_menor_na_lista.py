#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

print('\033[1;32m='*5,' Maior e menor valor em uma lista','='*5,'\033[m')

valores = []
maior = 0
menor = 0

for c in range (0,5):    # esse comando criou a var c que ira de 1 até 5
    valores.append(int(input('Digite os valores: '))) # aqui .append colocará os valores que o usuário digitar na lista criada vazia da var valores , rodará no loop acima 5 vezes (5 valores serão add a lista)
    if c == 0:                        # Se o c for igual ao primeiro valor recebido 0 logo o valor sera o maior r menor aommesmo tempo pois só tem ele
        maior = menor =valores[c]     # então as vars ,aior e menor recevem o valor
    else:                             # depois os valores vão passando no laço na var c então:
        if valores[c] > maior:        # se o valor que passou for maior que o valor que estava na var maior a var maior recebe este valor e assim aconteceta durante a passagem de todos os valores  , ficando assim no final a var maior com o maior valor
            maior = valores[c]        # a mesma coisa acontecerá para a var menor ficando com o menor valor
        if valores[c] < menor:
            menor = valores[c]
print(valores)
print(f' O maior valor foi {maior} na posição : ',end='')
for c, v in enumerate(valores):
    if v == maior:
        print(f'{c}...',end='')
print()
print(f' O menor valor foi {menor} na posição:  ',end='')
for c, v in enumerate(valores):
    if v == menor:
        print(f'{c}...',end='')

print()






