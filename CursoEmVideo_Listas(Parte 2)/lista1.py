"""
Faça um programa que leia nome e peso de várias pessoas
guardando tudo em uma lista.
No final, mostre:

a: quantas pessoas foram cadastradas.
b: uma listagem com as pessoas mais pesadas
c: uma listagem com as pessoas mais leves

Obs.: Gerar uma lista com os mais leves e mais pesados
Vai depender de analisar qual é o mais leve e o mais pesado.
Se houver mais de um com esse peso, insere na lista.
O mais normal é que a lista de mais pesados tenha apenas 1 pessoa,
que é o motivo pelo qual a lista existe.

"""

people_count=0
heavier=[]
less_heavy=[]
people=[]
peoples=[]
bigger=0
light=0

while True:
    people.append(str(input("Nome: ")))
    people.append(float(input("Peso: ")))
    people_count+=1

    for peso in people:
        if people[1]>100:
           heavier.append(peso)
        elif people[1]<60:
            less_heavy.append(peso)
            
    peoples.append(people[:])
    people.clear()
    
    d=str(input('Continuar?: '))
    if d =='s' or d=='S':
        print('Vamos continuar!!!')
    elif d=='n' or d=='N':
        break
    


print(f'Foram cadastradas {people_count} pessoas')
print(peoples)
print(f'Pessoas mais pesadas: {heavier}') 
print(f'Pessoas mais leves: {less_heavy}')

