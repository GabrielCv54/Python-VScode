student={}
n=[]


def notes(situation=False):
     cn=0
     while True:
        note=float(input('Nota : '))
        n.append(note)
        cn+=1
        student['Quantidade de Notas: '] = cn
        student['Maior nota'] = max(n)
        student['Menor Nota'] = min(n)
        student['Média'] = (sum(n)/len(n))
        if situation == True:
            if student['Média'] >=0 and student['Média'] <=4:
             student['Situação'] = 'Reprovado' 
            elif student ['Média'] >=5 and student['Média'] <6:
              student['Situação'] = 'Recuperação'
            elif student['Média'] >=6 and student['Média'] <=10:
               student['Situação'] = 'Aprovado'
        elif situation == False:
             student['Situação']  = ''
        d=str(input('Deseja continuar?: '))
        if d =='S' or d == 's':
            print('Vamos continuar!')
        else:
            break
     print(student)


notes()

