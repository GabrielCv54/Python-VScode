'''def counter(i,f,p):
    """
    ->Faz uma contagem e mostra na tela
    :param i: início da contagem
    :param f:fim da contagem
    :param p:passo da contagem
    :return: sem retorno
    
    """
    c=i
    while c<=f:
        print(f'{c}',end='')
        c+=p
    print('fim')

help(counter)'''


'''def sum(a,b,c=0):
    s= a+b+c
    print(f'A soma equivale a {s}')

sum(5,10)'''


'''def rest(b):
    global a
    a=9
    b+=4
    c=2
    print(f'C dentro vale {c}')
    print(f'B dentro vale {b}')
    print(f'A dentro vale {a}')


a = 5
rest(7)
print(f'A fora vale {a}')'''


'''def somar(a=0,x=0,c=0):
     s = a+x+c
     print(f'A soma vale {s}')
     return s

resp = somar(55,10,6)
print(resp)'''


'''def factorial(num=1):
   f = 1 
   for i in range(num, 0, -1):
      f *= i
   return f

f1 = factorial(9)
f2 = factorial(5)
f3 = factorial(4)
print(f'Os resultados são {f1},{f2} e {f3}')'''

'''n=int(input('Digite um número: '))
print(f'O fatorial de {n} é {factorial(n)}')'''

def par(num=0):
    if num % 2 ==0:
        return True
    else:
        return False

n=int(input('DIgite um numero: '))
if par(n) :
    print('É par!!')
else:
    print('Não é par!!')

    