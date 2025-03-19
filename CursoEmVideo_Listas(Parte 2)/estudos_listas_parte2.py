test=list()
test.append('Louis')
test.append(26)
gente=list()
gente.append(test[:])
test[0] = 'Oscar'
test[1] = 66
gente.append(test[:])
print(gente)

#galera=[['Igor',15],['Paulo',36],['teresa',28]]
#print(galera[0][1])

'''galera=list()
dado=list()
maior=0
menor=0

for contador in range(0,4):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
    
for i in galera:
    if i[1]>18:
        print(f'{i[0]} é de maior!')
        maior+=1
    else:
        print(f'{i[0]} é de menor!')
        menor+=1

print(f'{maior} são maiores de idade!!')
print(f'{menor} são menores de idade!')'''



food = ['Arroz','Feijão','Bife','Salada de Alface']
desserts = ['Bolo de Chocolate']
food2 = food.copy()
print(food2)


people=['Jorge','Luca','Melissa','Pedrinho','Otávio']
people.append('Kira')
print(people)


other=[5,48,69,87,455,32,10,45,87]
people.extend(other)
print(people)

'''people.insert(5,'Lorrane')
print(people)'''

'''other.remove(5)
print(other)'''

'''tirado = other.pop(6)
print(other)'''

numbers=[258,741,236,987,45,225,415,1000,690,254]
'''numbers.clear()
print(numbers)
'''

'''numbers.reverse()
print(numbers)'''

for item in numbers:
    print(item)


