# Ler duas notas
# e mostrar a média
# mostrar msg
#aprovado se média >= 7
# 5.0 á 6.9 recuperação
# abaixo de 5.0 reprovado

print('\033[1;33m-'*9,'Calcúlo de Média final','-'*9,'\033[m')
n1 = float(input('\033[1;34mDigite a nota da primeira prova: '))
n2 = float(input('Digite a nota da segunda prova: \033[m'))
media = (n1 + n2) / 2
if media >= 7.0:
    print('\033[1;32m Sua média é {},Parabéns você foi aprovado!!!'.format(media))
elif media < 5.0:
    print('\033[31mSua média é {},Infelizmente você foi reprovado , não desanime e se esforce mais no próximo ano.'.format(media))
else:
    media == 5 or media <= 6.9
    print('\33[33mSua média é {} ,Você ficou em recuperação, estude para a prova final.'.format(media))