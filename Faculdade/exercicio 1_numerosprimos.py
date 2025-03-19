#Exercício 1: Números Primos
'''Crie um programa que encontre e imprima os 20 primeiros números primos.
Um número é considerado primo se ele é maior que 1 e possui exatamente
dois divisores: 1 e ele mesmo. Utilize um loop while para iterar até
encontrar 20 números primos e um loop for para contar a quantidade de
divisores de cada número.'''

n=1
cont=0
primos=[]

while cont<=20:
    cont+=1
    n+=1
    if n % 2 !=0 and n % 5 !=0 and n % 3!=0 or n==3 or n==5 or n==2:
     primos.append(n)
     n+=1
print(primos)