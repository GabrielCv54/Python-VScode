from Utilidades.moeda import Coin


price = float(input('Qual o preço do produto?: '))
print(f'{Coin.increase(price,15)}')
print(f'{Coin.decrease(price,20)}')
print(f'{Coin.double(price)}')
print(f'{Coin.half(price)}')
