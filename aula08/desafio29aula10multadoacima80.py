# Ler a velocidade do carro
# Se Ultrapassar 80 KM mostre uma msg dizendo que foi multado
# A multa vai cusatar R$7,00 por cada Km acima do limite

vel = int(input('Digite a velocidade que estava o carro:'))
if vel <= 80:
    print('Velocidade permitida, tudo ok.')
else:
    print('Essa velocidade não é permitida , você receberá uma multa no valor R${:.2f}'.format((vel-80)*7))