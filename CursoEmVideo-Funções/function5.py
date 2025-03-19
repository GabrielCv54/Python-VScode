from random import randint

numbers=[]

def raffle():
    for i in range(0,5):
      i = randint(0,100)
      numbers.append(i)
    print(numbers)


def sum_pair():
   sum=0
   for value in numbers:
    if value % 2 == 0:
      sum+=value
   print(sum)


raffle()
sum_pair()