#Lista ordenada sem repetições

order_list=list()
pos=0

for i in range(0,5):
  number=int(input(f'digite o {i+1} valor: '))
  if i==0 or number > order_list[len(order_list)-1]:
    order_list.append(number)
    print('Adicionado ao fim da lista')
  else:
    while pos < len(order_list):
      if number <= order_list[pos]:
        order_list.insert(pos,number)
        print(f'Adicionado na posição {pos} da lista')
        break
      pos += 1

print(order_list)