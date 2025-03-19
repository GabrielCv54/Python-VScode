try:
 file = int(input('Digite o valor inteiro de file: '))
 path = int(input('Path : '))
 calc = file/path
except ValueError as value:
 print(f'\033[0;31;47m O tipo de dado deve ser um inteiro')
except ZeroDivisionError as zero:
 print(f'\033[0;31;47mNão é possível realizar divisão por zero')
except Exception as error:
  print(F'\033[0;31;47m o erro foi {error.__class__.__cause__}')
else:
  print(f'O resultado é {calc:.2f}')
finally:
 print(f'fim do programa ')

'''def factorial(n):
    f = 1
    c=0

    for i in range(n,0,-1):
        f*=i

    while c > 0:
        c-=1
        f*=i
        print(f'{c}',end='')
        print('*'  if c>0 else '=',end='')
        return f'{factorial(n)}'

print(factorial(4))
'''
