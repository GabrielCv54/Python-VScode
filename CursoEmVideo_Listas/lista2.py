#Valores únicos em uma lista

values=list()

while True:
  value=int(input("Digite-os: "))
  if value in values:
      print("Nao vou adicionar, pois esse valor já existe!")
  else:
    values.append(value)

  pergunta=str(input("Deseja continuar?: "))
  if pergunta =='s' or pergunta=='S':
    print('Vamos continuar!!!')
  elif pergunta =='n' or pergunta=='N':
   break  


values.sort()
print(f"Você digitou os valores {values}")
