# LEr o comprimento de 3 retas
# Dizer se pode ou não formar um triângulo

# Condição de existência de um triângulo
# a+b > C
# b+c > a
# a+C > B
# Dizer se é triãngulo escaleno todos os lados diferente
# iSÓCELES  dois lados iguais
# Equilátero todos os ladis iguais
print('\033[1;32;4m--------- Condição de existência de um triângulo ---------\033[m')
la = float(input('Digite lado A do triângulo:').strip())
lb = float(input('Digite lado B do triângulo').strip())
lc = int(input('Digite la C do triângulo:').strip())

if la + lb > lc and lb + lc > la and la + lc > lb:                # end == '' esse comando fará com que não haja enter para ir para px linha .
   print("\033[0;30;44m É possível formar um triângulo ",end='') # botar cores no python \033  m    esse é o código , entre [ e o m vem os números para as cores tem que consultar a tabela dai estilo , texto e fundo na ordem com : separando 0:33:44
   if la == lb == lc:
      print('Equilatero.\033[m')
   elif la != lb and la != lc and lb != lc:
      print('Escaleno.\033[m')
   else:
      print('Isóceles.')
else:
   print('\033[1;31mNão formam um triãngulo.\033[m')
