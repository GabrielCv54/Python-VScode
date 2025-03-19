#Dividindo valores em várias listas

normal=list()

while True:
  pair=list()
  odd=list()
  normal.append(int(input(" ")))
  d=str(input("Deseja continuar?: "))
  if d =='s' or d=='S':
   print('Continue!')
  elif d=='n' or d =='N':
    break

for valor in normal:
  if valor % 2==0:
    pair.append(valor)
  else:
    odd.append(valor)


print(normal)
print(odd)
print(pair)