#Extraindo dados de uma lista

t=list()

while True:
   t.append(int(input('Digite o valor a ser adicionado na lista: ')))
   d=str(input("Deseja continuar?: "))
   if d =='n' or d=='N':
     break
   if d =='S' or d=='s':
    print('Continuando!')
   else:
    print('problema!!!')

reverso=t.sort(reverse=True)
print('###############################')
print(f'Foram digitados {len(t)} números')
print(f'Lista Completa: {t}')
if 5 in t:
  print(f"5 Está digitado na lista!!!")
else:
  print('Não há o valor 5 digitado na lista!!')  