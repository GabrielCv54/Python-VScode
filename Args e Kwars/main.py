#Só um pouco do meu estudo sobre args e kwargs

#args
'''def func_arg(arg,*args):
    print(f'Primeiro argumento: {arg}')

    for argumento in args:
        print(f'Argumento de *args : {argumento}')

func_arg(15,44,12,5477,9,3)'''

'''def adicao(*args):
    res = 0

    for arg in args :
        res += arg

    return res

print(adicao(4,80))
print(adicao(7,10))'''

'''def func(*args):
    for a in args:
        print(a)

func(9)
func(47,45,21)'''

'''def world_cup_titles(country,*titles):
   print(f'País : {country}')

   for title in titles:
      print(f'Ano : {title}')
   
world_cup_titles('Brasil','1958','1962','1970','1994','2002')
world_cup_titles('Argentina','1978','1986','2022')
'''
#kwargs

'''me = {'Nome' :'Gabriel','Idade':18,'Faculdade':'Impacta','Curso':'ADS'}

def func(**kwargs):
    for key,value in kwargs.items():
        print(f'{key} : {value}')

func(**me)'''

'''def concat(**kwargs):
    print(f'Valores recebidos: {kwargs}')
    result =''

    for value in kwargs.values():
      result +=f' {value}'
    return result

print(concat(a='Gabriel',b='Carvalho',c='Vieira'))'''

def calculate_price(value,**kwargs):
    taxa_for_cent = kwargs.get('taxa_for_cent')
    discount = kwargs.get('desconto')

    if taxa_for_cent:
        value += value * (taxa_for_cent/100)
    if discount:
        value -= discount
    return value

preço_final = calculate_price(100,taxa_for_cent=40)
print(preço_final)

