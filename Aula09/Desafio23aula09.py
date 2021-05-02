#Ler número de 0 a 9999 e mostrar na tela os digitos separados
#unidade,dezena,centena,milhar

num = (input('Digite um número de 0 á 9999:'))
n =str(num)
print('Analisando número{}'.format(num))
print('Unidade = {}'.format(n[3]))
print('dezena = {}'.format(n[2]))
print('centena = {}'.format(n[1]))
print('Milhar = {}'.format(n[0]))


