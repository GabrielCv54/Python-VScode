from ex6.utilidades.Moeda import Coin
from ex6.utilidades.dado import read_money

price = read_money(input('Digite o valor: '))
Coin.resume(price,10,50)
print(read_money(price))
