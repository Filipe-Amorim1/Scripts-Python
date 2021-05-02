# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
# o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# # A) quantas pessoas tem mais de 18 anos.
# # B) quantos homens foram cadastrados.
# # C) quantas mulheres tem menos de 20 anos.
tot18 = 0
totm20= 0
toth =0
while True:
    idade = int(input('Idade: '))
    sexo =''
    while sexo not in 'MF':
        sexo = str(input('Sexo [M] ou [F]')).strip().upper()[0]
    if idade >= 18:
        tot18 = tot18 +1
    if sexo == 'M':
        toth +=1
    if sexo == 'M' and idade < 20:
        totm20 +=1
    resp = ''
    while resp not in 'SN':
        resp = str(input('Quer continuar? S ou N:'))
    if resp == 'N':
        break
print(f'Total de pessoas maiores de 18 {tot18}')
print(f'Total de mmulheres com menos de 21 anos é {totm20}')
print(f'TOtal de de homens cadastrados foi {toth}')



