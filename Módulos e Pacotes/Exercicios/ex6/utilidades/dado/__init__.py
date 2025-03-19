from utilidades.Moeda import Coin
from exceções import Erro_Type


def read_money(num):
    if type(num)!=float:
        raise Erro_Type('O numero só deve ser float')
    else:
        print(f'{Coin.increase(num,15)}')
        print(f'{Coin.decrease(num,20)}')
        print(f'{Coin.half(num)}')
        print(f'{Coin.double(num)}')