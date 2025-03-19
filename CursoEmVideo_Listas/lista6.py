#Validando expressões matemáticas


math=str(input("Escreva a expressão matematica: "))
pile=[]

for simbol in math:
    if simbol == '(':
        pile.append('(')
    elif simbol ==')':
        if len(pile)>0:
            pile.pop()
        else:
            pile.append(')')
            break

if len(pile) == 0 :
    print('expressão correta!')

else:
    print('Expressão errada!!')

