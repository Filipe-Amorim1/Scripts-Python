# Calcular o IMC
# LEr peso, ALtura
# Abaixo de 18.5 = abaixo do peso
# Entre 18.5 e 25 Peso ideal
# 25 até 30 Sobrepeso
# 30 até 40 Obeso
# Acima de 40 obesidade morbida

print('\033[33m --------- Calculo de IMC --------- ')
alt = float(input('\033[35mDigite a sua altura: '))
peso = float(input('Digite o seu peso: '))
imc = peso / (alt*alt)
print('O seu IMC é {:.1f}'.format(imc))
if imc > 40 :
    print('Muito Cuidado!!! Você está com Obesidade morbida.')
elif imc > 30 and imc <= 40:
    print('Cuidado! ,Você está obeso.')
elif imc >= 25 and imc <= 30:
    print('Você está com Sobrepeso.')
elif imc >  18.5 and imc <25 :
    print('Você está no Peso Ideal.')
else:
    print('Abaixo do peso.')





#O IMC é a relação entre peso e altura e o cálculo é feito de acordo com a
# fórmula:
# IMC = peso/ (altura x altura),
# devendo o peso estar em kg e a altura em metro, e o resultado é dado em kg/m2. Depois de obter o resultado,
# é verificado em que faixa o resultado se encontra, podendo indicar:
#Magreza, quando o resultado é menor que 18,5 kg/m2;
#Normal, quando o resultado está entre 18,5 e 24,9 kg/m2;
#Sobrepeso, quando o resultado está entre 24,9 e 30 kg/m2;
#Obesidade, quando o resultado é maior que 30 kg/m2.

