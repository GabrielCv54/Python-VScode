from datetime import datetime


def voto():
     '''
     -> Faz
     '''
     year_nasc = int(input('QUal o ano do seu nascimento?: '))
     age=(datetime.now().year)- year_nasc
     if age < 16:
          return f'Com {age} anos: Não precisa Votar'
     elif age>=18 and age<65:
         return  f'Com {age} anos: Voto Obrigatório'
     elif age>105:
          return f'Desculpe,mas essa pessoa provavelmente está morta!'
     else:
          return f'Com {age} anos: Voto Opcional'


response = voto()
print(response)