#Aprovar empréstimo bancário para a compra de uma casa
# Perguntar valor da casa
# Salário do comprador
# E em quantos anos ele vai pagar
# calcule a prestação mensal
# Não pode exceder 30% do salário
# se Exceder o empréstimo sera negado
print ('\033[33m-'*9 ,'Calcúlo Aprovação de Empréstimo','-'* 9) # \033[ m código para colocar cor o número  do meio 33 é o c´´odigo da cor
v_casa = float(input('Qual o valor da casa: ').strip())
sal = float(input('Qual o seu salário: ').strip())
anos = int(input('Quantos meses você pretende realizar o pagamento: \033[m')) # no fim o código da cor vazio para encerar a cor até aqui
porc_sal = sal * 0.3
calc_prest = float(v_casa / anos)

if calc_prest >= porc_sal:
    print('\033[33m Seu empréstimo foi negado , pois a prestação de R${:.2f} excede 30% do seu salário.'.format(calc_prest))
else:
    print('\033[35m Empréstimo aprovado , a prestação será de: R${:.2f}.'.format(calc_prest))