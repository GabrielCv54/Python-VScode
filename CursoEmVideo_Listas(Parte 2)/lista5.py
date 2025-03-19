"""
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.

O programa vai perguntar quantos jogos serão gerados
e vai sortear 6 números entre 1 e 60 para cada jogo,
cadastrando tudo em uma lista composta.
"""
from random import randint
from time import sleep 

games=[]
games1=[]
game=int(input('Quantos jogos você deseja?: '))
total=1

while total <= game:
    cont=0
    while True:
        random = randint(1,60)
        if random not in games:
           games.append(random)
           cont+=1
        if cont >=6:
            break

        #games.sort()
    games1.append(games[:])
    games.clear()
    total += 1

for i, list in enumerate(games1):
    print(f'Jogo {i+1} : {list}')
    sleep(2)
    
        
print('Bom jogo!!')