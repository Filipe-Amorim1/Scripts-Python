# Faça um programa que leia o sexo de uma pessoa, mas só aceite
# os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''sexo = str('')
while sexo not in 'F''M':'''
sexo= str(input('Digite seu sexo [ M/F ]: ')).strip().upper()[0] # strip para tirar os espaços , upper para jogar para miúscula e [0] para pegar a primeira letra do upper
while sexo not in 'MmFf':  # enquanto a var sexo  não estiver dentro(not in) da condição 'MnFf' escrevera Dados inv. e pedira para digitar novamente até atender a condição que sera uma da letra 'MmFf'
    sexo = str(input('Dados inválidos. Por favor informe seu sexo:  ')).strip().upper()[0]
print('Sexo {} registrado com sucesso '.format(sexo)) # Caso a condição for satisfeita o laço terminará e aparecerá o print



