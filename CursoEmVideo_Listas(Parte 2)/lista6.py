"""
Crie um programa que leia nome e duas notas de vários alunos
e guarde tudo em uma lista composta.

No final, mostre um boletim contendo a média de cada um
e permita que o usuário possa mostrar as notas de cada aluno individualmente

"""

"""
Cria um programa que lê nome e duas notas de vários alunos
e guarda-os numa lista completa.
"""


students=list()

while True:
    student=str(input('Nome do Aluno(a): '))
    score=float(input('Nota 1 do Aluno(a): '))
    score2=float(input('Nota 2 do Aluno(a): ')) 
    media = ((score+score2)/2)
    students.append([student,[score,score2],media])
    cond=str(input('Deseja Continuar?: '))
    if cond=='S' or cond=='s':
        print('Continuando')
    elif cond=='N' or cond=='n':
        break
    
#print(students)
print(f'{'N°':<4}{'Nome:':<10}{'Média':>8}')
for index,student in enumerate(students):
    print(f'{index:<4}{student[0]:<10}{student[2]:>8}')

while True:
    d=int(input('Qual aluno você deseja ver as notas?: '))
    #if d == 0:
      #  break
    if d <= len(students)-1:
        print(f'Notas de {students[d][0]} são {students[d][1]}')
    else:
        break

