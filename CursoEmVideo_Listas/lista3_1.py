list=list()
position=0


for i in range(0,5):
    num=int(input(f"{i+1}°Número: "))
    if i == 0 or num > list[len(list)-1]:
        list.append(num)
        print('Vamos adicionar no final da lista')
    else:
        while position<=len(list):
            if num <= list[position]:
                list.insert(position,num)
                print(f'Adicionado na posição {position}')
                break
            position+=1
    
print(list)