# LEr o comprimento de 3 retas
# Dizer se pode ou não formar um triângulo

# Condição de existência de um triângulo
# a+b > C
# b+c > a
# a+C > B
la = float(input('Digite lado A do triângulo:').strip())
lb = float(input('Digite lado B do triângulo').strip())
lc = int(input('Digite la C do triângulo:').strip())

if la + lb > lc and lb + lc > la and la + lc > lb:
    print("\033[0;30;44m É possível formar um triângulo") # botar cores no python \033  m    esse é o código , entre [ e o m vem os números para as cores tem que consultar a tabela dai estilo , texto e fundo na ordem com : separando 0:33:44
else:print('\33[0:30:41m Não formam um triângulo')



