#Ler o ano de nascimento de um aluno e mostrar  sua categoria
# de acordo com as idades:
#  4 Até 9 anos Mirim
# Até 14 anos infantil
# 19 anos Junior
# 20 anos Sênior
# acima de 20 master
from datetime import date
print('\033[1;35m****** Informação de Categoria ******')
data_atual = date.today().year
nasc = int(input('\033[1;32mDigite o ano do seu nascimento: '))
idade = data_atual -nasc
if idade < 9 and idade >= 4:
    print('Você tem ou fará {} anos em {} , sua catagoria é \033[1;34mMIRIM\033[m.'.format(idade,data_atual))
elif idade > 9 and idade <= 14:
    print('Você tem ou fará {} anos em {} , sua catagoria é \033[1;34mINFANTIL\033[m.'.format(idade, data_atual))
elif idade > 14 and idade <= 19:
    print('Você tem ou fará {} anos em {} , sua catagoria é \033[1;34mJUNIOR\033[m.'.format(idade, data_atual))
elif idade == 20:
    print('Você tem ou fará {} anos em {} , sua catagoria é \033[1;34mSENIOR\033[m.'.format(idade, data_atual))
elif idade > 20:
    print('Você tem ou fará {} anos em {} , sua catagoria é \033[1;34mMASTER\033[m.'.format(idade, data_atual))
elif idade < 4 and idade >=0:
    print('VocÊ ainda não tem idade para se inscrever,aguarde mais {} anos.'.format(4-idade))
else:
    print('Data inválida')


