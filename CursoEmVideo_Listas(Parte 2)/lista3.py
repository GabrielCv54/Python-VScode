"""
Crie um programa que crie uma matriz 3.3
e preencha com valores lidos pelo teclado.

No final, mostre a matriz na tela com a formatação correta
"""


matrix=[[0,0,0],[0,0,0],[0,0,0]]

for i in range(0,3):
    for c in range(0,3):
        matrix[i][c]=int(input(f'Digite um numero pra ser adicionado na posição[{i}][{c}]: '))

for i in range(0,3):
    for c in range(0,3):
        print(f'[{matrix[i][c]}]',end=' ')
    print()
