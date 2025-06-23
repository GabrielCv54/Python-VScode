import pandas as pd

def menu():
    users = []
    dici = {}
    try:
        while True:
            print('*'*65)
            print()
            print('1- Cadastrar alguma pessoa?: ')
            print('2- Mostrar todas as pessoas cadastradas!!')
            print('3- Sair ')
            print() 
            print('*'*65)
            option = int(input('Escolha uma das opções acima: '))
            if option == 1 :
                name = str(input('Qual seu nome?: '))
                age = int(input('Qual a sua idade?: '))
                dici['Nome'] = name
                dici['Idade'] = age
                users.append(dici)
                print(users)
                '''df = pd.DataFrame(dici)
                print(df)'''
            elif option == 2:
                for i in range(len(users)):
                    print('*'*65)
                    print(f'{users[i]:<10} | {users[i]:>20}')
                    print('*'*65)
            elif option == 3:
                break    
            elif option not in [1,2,3] :
                print('Não existe essa opção!!')

    except Exception as error: 
        print(f'Dados sobre o erro : {error}')
    except KeyboardInterrupt :
        print('\nInterrupção pelo usuário')

    else:
        print('Finalizado')


def converter_excel():
    pass

if __name__ == '__main__':
    menu()