def my_function(**kid):
  print(f"O seu último nome { kid["lname"]},e ele possui {kid['age']} anos")

my_function(fname = "Tobias", lname = "Refsnes",age=22)



def retorno(x):
  return 44 / x

print(retorno(x=85))