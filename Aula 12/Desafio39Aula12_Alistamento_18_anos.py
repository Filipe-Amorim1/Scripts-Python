# Ler o ano de nascimento
# Informar de acordo com a idade
# Se ele ainda vai se alistar ao serviço militar
# Se é a hora de se alistar
# Se já passou do tempo de alistamento
# Dizer o tempo que falta ou se já passou do tempo

print("\033[1;31m-"*6,'\033[1;36mConsulta prazo para alistamento no serviço militar\033[m','\033[1;31m-\033[m'*6)  # \033[m para terminar a formatação e cor , o ns números no meio entre [ e m é os códigos de cores e formatação divididos por
from datetime import date
nasc = int(input('Digite o ano do seu nascimento: '))
dataatual = date.today().year
idade = dataatual - nasc
print('Quem nasceu em {} tem(ou completará) {} anos em {} '.format(nasc,idade,dataatual))
if idade == 18:
    print('Você deve se alistar este ano.')
elif idade < 18:
    print('Você ainda não tem 18 anos ,falta {} anos para você se alistar'.format(18-idade))
else:
    idade > 18
    print('Você já deveria ter se alistado há {} anos.Em {} você deveria ter se alistado.'.format((idade-18),(nasc+18)))


# dataatual = ('{}/0{}/{}'.format(dataatual.day,dataatual.month,dataatual.year))
#esse método é opção mais o .strftime evita complicações caso o mês fosse maior que 9 o zero que colocamos ia ficar 010
#dataatual = dataatual.strftime('%d/%m/%y')
#print(dataatual)
#Formatando datas em strings usando o método strftime()
#para evitar maiores complicações, a classe date soluciona isso com um único método -
# o strftime(), que toma como parâmetro a formatação que queremos em nossa string de data e,
# desse modo, nos dá maior liberdade para decidirmos como queremos exibir a data.
#Esta formatação usa códigos melhor explicados na documentação. Ao final do texto,
# também damos uma explicação breve neles. No nosso caso fica assim:
#data_em_texto = data_atual.strftime(‘%d/%m/%Y’)
#print(data_em_texto)
#E agora sim#

