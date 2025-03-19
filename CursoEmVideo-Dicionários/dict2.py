from random import randint
from operator import itemgetter
from time import sleep

plays={}
ranking=list()

for i in range(0,4):
    plays[f'Jogador {i+1} '] = randint(1,6)
    sleep(1)
    ranking=sorted(plays.items(),key=itemgetter(1),reverse=True)
print('====Ranking=====')
print(f'{'Rank':<4}  {' Jogador':11} {'Número':>8}')
for index,value in enumerate(ranking):
    print(f'{[index+1]}° - {[value]}',end='')
    print()
    


'''    for i in range(0,4):
        print(f'{i+1}°Lugar: ',end='')
        print(plays.keys())
        sleep(1)'''

     
'''print(plays)
print(ranking)'''