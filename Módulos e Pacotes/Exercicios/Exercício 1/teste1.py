from ex1 import Coin

price = float(input('Qual o preço?: '))

print(f'A metade de {price} é {Coin.half(price)}')
print(f'O dobro de {price} é {Coin.double(price)}')
print(f'Aumentando em 5% é {Coin.increase(price,10)}')
print(f'DIminuindo em 15% é {Coin.decrease(price,13)}')