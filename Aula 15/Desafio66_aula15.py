#Crie um programa que leia números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999,que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

num =0
cont = 0
soma = 0

while True:
    num= int(input('Digite um número: '))
    if num == 999:
        break
    soma = soma + num
    cont = cont +1
print(f'Você digitou {cont} números , a soma estre eles foi {soma}')