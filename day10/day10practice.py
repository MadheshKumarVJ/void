try:
  name=input()
  age=int(input())
  if age>=18:
    print("you can vote")
  elif age>0 and age<18:
    print("you can't vote")
  else:
    print("give a valid age")
except ValueError as e:
  print("give a valid age")