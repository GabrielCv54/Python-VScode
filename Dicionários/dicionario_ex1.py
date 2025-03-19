#Exercicio 1
produtos={}

p1=(input("Produto 1: "))
v1=float(input("Valor do produto 1 : "))
p2=(input("Produto 2 : "))
v2=float(input("Valor do produto 2: "))
p3=(input("Produto 3: "))
v3=float(input("Valor do produto 3: "))
p4=(input("Produto 4: "))
v4=float(input("Valor do produto 4: "))
p5=(input("Produto 5: "))
v5=float(input("Valor do produto 5: "))

produtos[p1]=v1
produtos[p2]=v2
produtos[p3]=v3
produtos[p4]=v4
produtos[p5]=v5

for chave,valor in produtos.items():
 if valor>50.00:
  print("Produto que custa mais que 50: ")
  print(f'{chave},')