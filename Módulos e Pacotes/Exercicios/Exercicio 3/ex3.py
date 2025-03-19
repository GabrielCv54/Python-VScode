class Coin:
    def increase(num,aument,p):
        if p == True: 
         return f'{num + (num*(aument/100)):.2f}'
        elif p == False:
            return num + (num*(aument/100))
    
    def decrease(num,diminute,p):
        if p == True: 
         return f'{num - (num*(diminute/100)):.2f}'
        elif p == False:
           return num -(num*(diminute/100))
    
    def half(num,p):
        if p == True:
           return f'{num / 2:.2f}'
        elif p == False: 
         return num / 2
    
    def double(num,p):
        if p == True:
            return f'{(num * 2):.2f}'
        elif p == False: 
         return f'{num * 2}'