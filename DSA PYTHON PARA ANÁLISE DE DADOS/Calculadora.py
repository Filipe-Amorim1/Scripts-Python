a = int(1)
b = int(1)


a = int(input('Digite um número'))
b = int(input('Digite um número'))

soma = a + b
multi = a * b
sub = a - b
div = a / b
porc = a + (b/float(100))
pot = a**b
print ('''Digite
(1) Somar
(2) Multiplicar
(3) Subtrarir
(4) Dividir
(5) Porcentagem
(6) Potência ''')
s = int(input('opção: '))
if s == 1:
    print(soma)
elif s == 2:
    print(multi)
elif s == 3:
    print(sub)
elif s == 4:
    print(div)
elif s == 5:
    print(porc)
elif s == 6:
    print(pot)
else:
    print('opção Inválida')
