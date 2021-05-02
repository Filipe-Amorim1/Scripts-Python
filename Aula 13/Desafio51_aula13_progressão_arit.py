# Mostrar a progressão aritimética
# LEr o primeiro termo e a razão
# MOstre os 10 primeiros termos dessa progressão
n = int(input('Digite o início da progressão: '))
r = int(input('Digite a razão da progressão: '))
for c in range(n,r*10,r):
    print(c)
print('\033[1;32mAcabou')
