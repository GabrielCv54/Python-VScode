from ex2 import Coin

price = float(input('Qual o preço?: '))

print(f'O aumento de 15% é {Coin.increase(price,15):.2f}')
print(f'Diminuindo 20%  é {Coin.decrease(price,20):.2f}')
print(f'O dobro de {price} é {Coin.double(price):.2f}')
print(f'A metade de {price} é {Coin.half(price):.2f}')