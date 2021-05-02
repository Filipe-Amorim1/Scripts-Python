# Perguntar a distãncia da viagem em Km
# Cobrar R$0,50 para viagens até 200 km
# cobrar R$0,45 para viagens mais longas

dist = int(input('Digite a quilometragem da sua viagem: ').strip())
if dist <= 200:
    print('O valor da sua viagem é R${:.2f}'.format(dist*0.50))
else:print(('O valor da sua viagem é R${:.2f}'.format(dist*0.45)))