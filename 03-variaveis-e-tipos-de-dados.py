'''
Variável: espaço na memória para armazenar um
dado para ser usado várias vezes
'''

aluno = {   # Isso é um dicionário
    'name': 'Alexsandro Felix',
    'age': 43,
    'weight': 65.8,
    'enable': True
}

for k in aluno.keys():  # loop usando 'for'
    print('A variável "%s" contém "%s" e é do tipo %s' %
          (k, aluno.get(k), type(aluno.get(k))))
    print('=' * 72)
