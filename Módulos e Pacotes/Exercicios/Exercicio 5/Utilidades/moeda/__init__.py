class Coin:
    def increase(n,up):
        return( f'15% de Aumento : {n + (n * (up/100)):.2f}')
    
    def decrease(n,diminute):
        return f'20% de redução : {n - (n * (diminute/100)):.2f}'
    
    def half(n):
        return f'Metade do Valor : {n / 2:.2f}'
    
    def double(n):
        return f'Dobro do valor : {n * 2:.2f}'
    
    def resume(n,up,diminute):
        print(Coin.increase(n,up))
        print(Coin.decrease(n,diminute))
        print(Coin.half(n))
        print(Coin.double(n))