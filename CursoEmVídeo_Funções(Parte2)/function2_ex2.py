from math import factorial

def fatorial(show):
    '''
    -> Calcula o fatorial de um número digitado 
    :var number : Número do qual desejo calcualr o fatorial.
    :param show: define se será mostrado o resultado do fatorial,
    ou o processo da conta inteira.
    :param return : Retorna o valor do fatorial ou o processo.
    '''
    number = int(input('Número : '))
    f=1
    cont=number

    for i in range(number,0,-1):
       f*=i

    if show == False:
        return f'{factorial(number)}'
    elif show == True:
        while cont > 0:
         print(f'{cont}',end='')
         print(' * ' if cont>1 else' = ',end='')
         cont-=1
         f*=cont             
        return f'{factorial(number)}'  
    else:
        raise TypeError('Só pode ser verdadeiro o falso')
    

response = fatorial(True)
print(response)
#print(help(fatorial))