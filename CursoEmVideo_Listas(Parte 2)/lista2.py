"""
Crie um programa onde o usuário possa digitar
sete valores numéricos
e cadastre-os em uma lista única
que mantenha separados os valores pares e ímpares.

No final, mostre os valores pares e ímpares
em ordem crescente.
"""

numbers=[]
odd=[]
pair=[]


for i in range(0,7):
    number=(int(input(f'Digite o {i+1}° valor: ')))
    if number % 2 == 0:
        pair.append(number)
        pair.sort()

    else:
        odd.append(number)
        odd.sort()
  
    numbers.append(odd[:])
    numbers.append(pair[:])

#print(f'{numbers}')
print(f'Os números ímpares são : {odd}')
print(f'Os números pares são : {pair}')