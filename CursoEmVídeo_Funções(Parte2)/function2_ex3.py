def record():
    '''
        
    '''
    name = str(input('Nome do Jogador?: '))
    goals = str(input('Quantos gols ele fez?: '))
    if name == '':
        name='<desconhecido>'
        if goals =='':
         goals = 0
    return f'{name} fez {goals} gols no Campeonato'


romario = record()
print(romario)