alunos=dict()


alunos['Nome ']=str(input('Nome: '))
alunos['Média ']=float(input('Média: '))
if alunos['Média '] >=6:
    alunos['Situação'] = 'Aprovado'
elif alunos['Média '] >=4 and alunos['Média ']<=6:
    alunos['Situação'] = 'Recuperação'
else:
    alunos['Situação'] = 'Reprovado'


for k,v in alunos.items():
    print(f' {k} : {v} ')