"""
Aprimore o desafio anterior, mostrando no final:

a: a soma de todos os valores pares digitados
b: a soma dos valores da terceira coluna
c: o maior valor da segunda linha
"""

matriz=[[0,0,0],[0,0,0],[0,0,0]]
sum_pair=0
sum_third=0


for line in range(0,3):
    for column in range(0,3):
        matriz[line][column]=int(input(f'Digite um número da posição [{line}][{column}]: '))

for item in matriz[2]:
    sum_third+=item

for line in range(0,3):
    for column in range(0,3):
         if matriz[line][column] % 2==0:
          sum_pair+=matriz[line][column]

print(f'A soma de todos os pares é {sum_pair}')
print(f'A soma dos valores da terceira coluna é {sum_third}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')
for i in range(0,3):
    for c in range(0,3):
        print(f'{matriz[i][c]}',end=' ')
    print()