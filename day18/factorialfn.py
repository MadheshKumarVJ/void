def factorial(a):
  fact=1
  while  a>0:
    fact=fact*a
    a-=1
  print(fact)

n=int(input("enter a number:"))
factorial(n)