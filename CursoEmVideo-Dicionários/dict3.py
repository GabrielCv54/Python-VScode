from datetime import datetime

work=dict()

current_year=datetime.now().year 

work['Nome'] = str(input('Nome: '))
work['Ano de Nascimento']= int(input('Ano de Nascimento: '))
work['Idade'] = datetime.now().year - work['Ano de Nascimento']
work['Carteira'] = int(input('Carteira de Trabalho: '))
if work['Carteira']!=0: 
  work['Ano de Contratação']= int(input('Ano de contratação: '))
  work['Salário'] = float(input('Salário: '))
  work['Aposentadoria'] = work['Idade']+ ((work['Ano de Contratação'] + 35) - current_year)
  age=current_year-work['Ano de Nascimento']
  print('=='*20)
for k,v in work.items():
  print(f'{k} : {v}')


else:
  print('---------------------')
  print(f'{work}')




#print(age)