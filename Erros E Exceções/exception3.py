import csv

column = ['Herói','Poder','Defesa','Ataque']

line=[['Batman','Tecnologias alto-potentes',80,75]]

with open('registro.csv','w',newline='',encoding='utf-8') as csv_archive:
    writer = csv.writer(csv_archive,delimiter='|')
    writer.writerow(column)
    writer.writerows(line)

print('-'*30)
print('Menu')
for value in 'registro.csv':
    print(f'{}')
