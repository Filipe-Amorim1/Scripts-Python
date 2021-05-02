print('\033[1;33m-------- Teste de Maioridade -------- \033[m')
from datetime import date # importamos a bibliotéca data
data_atual = date.today().year # var vai recebar a data atual do PC
totalmaior = 0   # var criadas para serem contadoras , vai contar quantas vezes no laço a idade foi maior ou igual a 21.
totalmenor = 0   # var criadas para serem contadoras ,vai contar quantas vezes no laço a idade foi menor q 21.


for pess in range(1,8):
    ano_nasc = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(pess)))
    idade = data_atual-ano_nasc
    if idade >= 21:
        totalmaior = totalmaior + 1
    else:
        totalmenor = totalmenor + 1
print('Total de {} pessoas com maioridade.'.format(totalmaior))
print('Total de {} pessoas menores de idade.'.format(totalmenor))





