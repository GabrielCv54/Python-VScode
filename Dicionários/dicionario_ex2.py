alunos={}
notas=[]

for i in range(1,6):
 ra=int(input(f"RA do {i}° aluno: "))
 n1=float(input(f"nota 1 do {i}°Aluno: "))
 notas.append(n1)
 n2=float(input(f"nota 2 do {i}°Aluno: "))
 notas.append(n2)
 n3=float(input(f"nota 3 do {i}°Aluno: "))
 notas.append(n3)
 media=((n1+n2+n3)/3)
 alunos[ra]=(notas)
 print(f"A média do aluno {i+1}° é {media:.2f}")
 print("====================================")
