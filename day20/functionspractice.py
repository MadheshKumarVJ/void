#prime Number
def PrimeNumber(number):
  count=0
  for i in range(1,n+1):
    if number%i==0:
      count+=1
  if count>2 or n==0 or n==1:
    return "Not a prime Number"
  else:
    return "Prime number"

n=int(input("Enter a number:"))
print(PrimeNumber(n))




#Sum of the digits of a number 
def Sumofdigits(number):
  sum=0
  while number>0:
    remainder=number%10
    sum+=remainder
    number//=10
  return sum


n=int(input("Enter a number:"))
print(Sumofdigits(n))


