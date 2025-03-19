#Exercício 2: Cálculo de Médias Ponderadas
'''Desenvolva uma função chamada calcular_medias que receba uma lista de
listas, onde cada sublista contém três notas de um aluno. A função deve
calcular a média ponderada de cada aluno, considerando pesos de 30%
para as duas primeiras notas e 40% para a terceira nota.
Retorne uma lista com as médias calculadas e imprima as notas dos alunos
junto com as respectivas médias.'''

def calcular_media(n1,n2,n3):
   media=((0.3*(n1+n2))+(0.4*(n3)))/3
   print(f'{media:.2f}')
   return media

notas=[]


for i in range(0,3):

   n1=float(input(f"Primeira nota do {i+1}° aluno: "))
   n2=float(input(f"Segunda nota do {i+1}° aluno: "))
   n3=float(input(f"Terceira nota do {i+1}° aluno: "))
   print(f"A média do {i+1}° aluno é: ")
   calcular_media(n1,n2,n3)
   print("-------------------------------------")

print(calcular_media)
