def read_int_and_float():
        integer = None
        while integer is None:
         try:
            integer_input = (input('Digite um inteiro: '))
            integer = int(integer_input)
         except ValueError:
                print('Só é possível aceitar inteiros!')       
         else:
              print(f'Inteiro : {integer}')


        decimal = None
        while decimal is None:
         try:
            decimal_input = (input('Digite um número float: '))
            decimal = float(decimal_input)
         except ValueError:
                print(' Erro! Só é possível aceitar números decimais!')                     
         else:
           print(f'Decimal : {decimal}')
              
      
read_int_and_float()