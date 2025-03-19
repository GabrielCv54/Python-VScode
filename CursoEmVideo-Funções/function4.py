from time import sleep

def bigger(*set):
    length = len(set)
    for value in set:
        sleep(1)
        print(value,end=' ',flush=True)
    print()
    print(f'Valores recebidos : {set} | Quantidade : {length}')
    maior = max(set)
    print(f'O maior valor é {maior}')
    print('='*60)


bigger(25,10,66,98,32,2,37)
bigger(24,18,789,63,28,45,47,13)
bigger(101,52,698,445,87,20,336)
bigger(108,1520,6325)
bigger(258,56,100,360,987)