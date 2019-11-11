# Soma
print('Operações de soma')
print('2 + 2 = ', 2 + 2)

# Multiplicação:
print('Operação de multiplicação')
print('2 * 3 = ', 2 * 3)

# Divisão (usando função):


def div(x, y):
    title = 'Operação de Divisão'
    res = x / y

    return print('%s\n%s / %s = %s' % (title, x, y, res))


div(8, 2)

# Expoenciação
print('Expoenciação\n - elevar um número à potência X')

print('2 ^3 = ', 2 ** 3)

# Módulo
print('Módulo é igual ao resto da divisão')
print('10 / 3 = ', 10 % 3)
