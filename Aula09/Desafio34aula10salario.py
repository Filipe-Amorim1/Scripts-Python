# Perguntar Salário de um funcionário
# calcular valor do aumento
# Salários superiores a R$1250  calcular aumento de 10%
# para inferiores ou iguais aumento de 15%

sal =  float(input('Digite seu salário:').strip())
if sal > 1250:
    print('Seu novo salário será: R${:.2f}'.format((sal*0.10)+sal))
else:
    print('Seu novo salário será:R${:.2f}'.format((sal*0.15)+sal))