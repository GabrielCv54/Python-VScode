players={}
lista=[]
goals=[]
c_goals=0

while True:
    players['Nome']=str(input('Digite o nome: '))
    players['Gols/Partida'] = []
    matches=int(input('Quantas partidas ele jogou?: '))
     
    for i in range(matches):
        goal=(int(input(f'Quantos gols ele fez na partida {i+1}: ')))
        players['Gols/Partida'].append(goal)
        

    players['Total de Gols'] = sum(players['Gols/Partida'])
    lista.append(players.copy())

    d=str(input('Deseja Continuar?: '))
    if d =='s' or d=='S':

        print('Vamos Continuar!!!')
    elif d=='N' or d=='n':
        break
      


for k,v in enumerate(lista):
    print(f'{k}------- {v}')

while True:
    d=int(input('Deseja ver o aproveitamento de qual jogador?: '))
    if d <= len(lista):
        print(f'{lista[d]}')
    if d == 999:
        print('Obrigado por nos consultar!!!')
        break 