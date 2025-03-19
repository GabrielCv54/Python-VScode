from time import sleep

def helper():
    function = str(input(f'\033[0;34;47m Função ou Biblioteca: '))
    print(f'\033[0;34;43m Propriedades do método ou biblioteca {function}')
    sleep(1)

    if function == 'fim':
        print('Acabou')
    else:
        help(function)
       


helper()



