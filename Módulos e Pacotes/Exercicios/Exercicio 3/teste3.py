from ex3 import Coin

preço = float(input('Preço : '))
print(f'Aumentando em 20% : {Coin.increase(preço,20,False)}')
print(f'Diminundo em 5% : {Coin.decrease(preço,5,False)}')
print(f'O dobro de {preço} é {Coin.double(preço,True)}')
print(f'A metade de {preço} é {Coin.half(preço,False)}')