#
def mostralinha():
    print('\033[1:33m-='*10,'\033[m')

mostralinha()
print('Filipe Amorim ')
mostralinha()

def soma(a,b):
    s = a+b
    print(s)

soma(7,8)
soma(b=5,a=5) # podemos escolher os parametos , atribuindo a eles os valores que queremos
soma(4,4)

mostralinha()
def soma(a,b):
    print(f'A = {a} e B = {b}')
    s = a+b
    print(f'a soma de A + B = {s}')
    mostralinha()

soma(7,8)
soma(b=5,a=5) # podemos escolher os parametos , atribuindo a eles os valores que queremos
soma(4,4)

# O * serve para desempacotar os parametros , podemos botar qunatos paramentros quiser sem dar erro .
def contador(*núm):
    tam = len(núm)
    print(f'Recebi os valores {núm} e o tamanho da lista é {tam}.')

contador(1,3,5,5)
contador(1,5,66)
contador(7)
mostralinha()

def dobra(list):
    pos = 0
    while pos < len(list):
        list[pos] *=2
        pos+=1

valores = [1,2,3,35,10]
dobra(valores)
print(valores)
