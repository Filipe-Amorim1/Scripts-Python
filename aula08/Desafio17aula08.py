#Calcule o comprimento do cateto adjascente e cateto oposto de um triângulo retaângulo  e mostre a hipotenusa
import math
ca = float(input('Digite o cateto adjascente:'))
co = float(input('Digite o cateto oposto:'))
hip = math.hypot(ca,co)
print('A hipotenusa dos catetos {} e {} é {}'.format(ca,co,hip))