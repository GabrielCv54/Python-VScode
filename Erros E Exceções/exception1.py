'''def red_int( ):
        integer=int(input('Digite: '))
        return integer

def red_float():
      decimal=float(input('Digite um float: '))
      return decimal'''


class Errodetipo(Exception):
    pass


    try:    
        integer = int(input('Digite um valor inteiro: '))
        decimal = float(input('Digite um float: '))  
      
    except ValueError:
        print('\033[0;31;40mSó é possivel ser escrito inteiro!')
        
    else:
            print(f'Inteiro : {integer}')
            print(f'Float:  {decimal}')
