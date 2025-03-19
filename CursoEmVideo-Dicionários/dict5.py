peoples=dict()
pessoas=list()
contF=0
adm=0
soma=0

while True:
    peoples['Nome']=str(input('Nome: '))
    peoples['Idade']=int(input('Idade: '))
    soma += peoples['Idade']
    peoples['Sexo']=str(input('Sexo: '))
    if peoples['Sexo'] =='f' or peoples['Sexo']=='F' :
        contF+=1 
    if peoples['Sexo'] != 'm'or peoples['Sexo']!='M' or peoples['Sexo'] != 'F' or peoples['Sexo']!='f':
        print('Só aceito m ou f')
    pessoas.append(peoples.copy())
    d=str(input('Deseja continuar?: '))
    if d=='S' or d=='s':
        print('Continuemos!!')
    elif d=='N' or d=='n':
        break


media = soma / len(pessoas)
for pessoa in pessoas:
     if pessoa['Idade'] > media :
        adm+=1

print(pessoas)
print(f' {len(pessoas)} pessoas foram cadastradas' )
print(f' A Média de idades é igual a {media:.2f} anos')
print(f' {contF} mulher(es) foram cadastradas:', end='')
for peoples in pessoas:
    if peoples['Sexo'] == 'f' :
     print(f' {peoples['Nome']}|',end='')
print()

print(f' {adm} pessoas tem idade acima da média')
for pessoa in pessoas:
    if pessoa['Idade']> media:
        print(f' {pessoa['Nome']} : {pessoa['Idade']}')

