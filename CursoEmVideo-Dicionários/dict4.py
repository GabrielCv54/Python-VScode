utilization={}
goals=[]
c_goals=0

utilization['nome']=str(input('Digite o nome: '))
matches=int(input('Quantas partidas ele jogou?: '))
for i in range(0,matches):
    goal=int(input(f'Quantos gols ele fez na partida {i+1}: '))
    goals.append(goal)
    c_goals+=goal

utilization['Gols por Partida']=goals
utilization['Total de Gols'] = c_goals

print(f'{utilization['nome']} jogou {matches} partidas')
print(utilization)