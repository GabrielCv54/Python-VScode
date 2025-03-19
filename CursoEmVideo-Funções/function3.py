from time import sleep

def contagem_definida(inicio,fim,passo): 
      while inicio > fim or inicio == fim:
           print(inicio,end=' ',flush=True)
           sleep(0.5)
           inicio-=passo

      while inicio < fim :
           print(inicio,end=' ',flush=True)
           sleep(0.5)
           inicio+=passo
      print('\n')



def counter():
     
          init = int(input('Qual seu início?: '))
          end= int (input('Qual seu final?: '))
          step = int(input('Qual seu passo?: '))
          
          while init>=end:
             init-=step
             print(f'{init}',end='=',flush=True)
             sleep(0.5)  

   
          while init<=end:
            init+=step
            print(f'{init}',end='=',flush=True)
            sleep(0.5)
       
                  
            #print('=====')


contagem_definida(1,10,1)
contagem_definida(10,0,2)   
help(counter)
