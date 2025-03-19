""" def title(txt):
    print('-'*30)
    print(txt)
    print('=='*25)

title('CURSO EM VíDEO') """


""" def soma(arg1,arg2):
    print(f'Arg1 é {arg1}, e Arg2 é {arg2}')
    soma = arg1+arg2
    print(soma)
    print('--'*15)

soma(arg1=2255,arg2=1414)
soma(25,17) """


""" def counter(* set):
   tam= len(set)
   print(f'Recebi os valores {set} e são {tam} números')


counter(2,15,20,36)
counter(21.5,10,6,32,88,74)
counter(12,66,33,5,10,8) """


""" def double(v):
     pos=0
     while pos<len(v):
        v[pos] *= 2
        pos+=1
      

values=[2,10,5.8,17,58,148,36,7.5]
double(values)
print(values) """


def sum(*n):
    s = 0
    for num in n:
        s+=num
    print(f'{s}')


sum(258,25)