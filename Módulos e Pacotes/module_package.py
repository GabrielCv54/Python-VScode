from uteis import double
from uteis import triple


def fatorial (num):
    f = 1

    for c in range(1,num+1):
        f*=c
    return f

num = int(input('Digite  o valor: '))
fat = fatorial(num)
d = double(num)
tri = triple(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {d}')
print(f'O triplo de {num} é {tri}')

