def red_int(n):
    if type(n)  == int:
          print(f'\033[0;34;40mVocê digitou um inteiro {n}')
    else:
       print('\033[0;33;41m Erro! Só é possivel um inteiro!!')

red_int(True)

