nome = str(input('Digite seu nome: ')).strip()
n = nome.capitalize()# vai colocar a tudo para a 1ª letra maiúscula
if n == 'Filipe':
    print('Que nome bonito você tem\ntenha um bom dia, {}!!'.format(n))
elif n == 'Pedro' or n == 'Maria' or n == 'Mario':
    print('Seu nome é comum no brasil\nTenha um bom dia, {}!!  '. format(n))
elif n == 'Natalie' or n =='Marina' or n == 'Jolie':
    print('Que belo nome feminino\nTenha um bom dia,',n,'!!!')
else:print('Bom dia, ',n,'!!!!')



# Como fizemos na linha 2 a váriavel n trasfomará a var nome com a 1º letra maiúscula independete de como o usuário escrever
# Então não podemos esquecer de colocar os nomes nos scripts com a 1º letra maiuscula se não o python não reconhecerá