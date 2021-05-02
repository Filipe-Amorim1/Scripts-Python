#Ler um angulo qualque e mostrar o valor sdo seno cosseno e tangente
import math
angulo = float(input('Digite o ângulo:'))
s = math.sin(angulo)
c = math.cos(angulo)
t = math.tan(angulo)
print('Seno {}\nCosseno {}\nTangente {}'.format(s,c,t))
