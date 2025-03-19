#Maior e menor valores
numeration=list()

for i in range(0,5):
  numeration.append(int(input("qual o número?: ")))
for c,v in enumerate(numeration):
  print(f"Na posição {c} encontrei o valor {v}") 


print(f"O maior valor é {max(numeration)} na(s) posição(ões)",end=' ')
for i,v in enumerate(numeration):
  if v == max(numeration):
    print(f"{i} ") 

  
print(f"O menor valor é {min(numeration)} na(s) posição(ões) ",end=' ')
for i,v in enumerate(numeration):
  if v==min(numeration):
    print(f'{i} ')

    