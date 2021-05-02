#Faça um programa que tenha uma função chamada área(),
# que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

print('='*30)
print('       CALCÚLO DE ÁREA')
print('='*30)
def área(l,c):
    x = l*c
    print(f' A área do terreno é {x:.2f} m².')
l = float(input('Qual a largura da área: '))
c = float(input('QUal o comprimento da área: '))

área(l,c)
