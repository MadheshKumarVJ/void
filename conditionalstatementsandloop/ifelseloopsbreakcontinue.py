number = 5
#If the condition is true the block of code inside the if statement gets executed
if number > 0:
    print('Number is positive')
print("hello")

#syntax of if-else statement:
if condition:
    # body of if statement
else:
    # body of else statement


number = 10
if number > 0:
    print('Positive number') #The statement gets printed the condition is true

else:
    print('Negative number') #The statement gets printed the condition is false


#Example: Python if…elif…else Statement
number = 0
if number > 0: #condition 1
    print('Positive number') #The statement gets printed the condition1 is true
elif number <0:
    print('Negative number')         print('Number is positive') 

else:
    print('Zero')  #The statement gets printed if both conditions are false


 number = 5
# outer if statement
if number >= 0:  #condition1 
    # inner if statement
    #Enters the inner if condition1 is true
    if number == 0:  #condition2
      print('Number is 0') #The statement gets printed the condition2 is true
    
    # inner else statement
    else:
        print('Number is positive') #The statement gets printed the condition2 is false
# outer else statement
else:
    print('Number is negative')   #The statement gets printed the condition1 is false



#Example program using if-else statement
grade=int(input("Enter your score out of 100:"))
if grade>=35:
    result="pass"
else:
    result="fail"
print(result)         


#The about code can also be written as
grade=int(input("Enter your score out of 100:"))
result="pass" if grade>=35 else "fail"


#For loop
languages = ['Swift', 'Python', 'Go']
# access elements of the list one by one
for i in languages:
    print(i)

#Example: Loop Through a String
language = 'Python'
# iterate over each character in language
for x in language:
    print(x)


#for Loop with Python range()
# iterate from i = 0 to i = 3
for i in range(4):
    print(i)

#program to compute the sum of n natural numbers using for loop
n=int(input("enter a number"))  
sum=0  
for i in range(1,n+1):
    sum+=i
print(sum)    


#Example: Program to find whether the given input is prime number or not
n=int(input("Enter a number:"))
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
if(count>2):
    print("Not a prime number")
else:
    print("Prime number")



#WHILE LOOP:
#In Python, we use the while loop to repeat a block of code until a certain condition is met
number = 1
while number <= 3:
    print(number)
    number = number + 1
    
#Example: Program to print factorial of a number using while loop
n=int(input("enter a number:"))
fact=1
while(n>0):
    fact*=n
    n-=1
print(fact)    



#Nested for loop
for i in range(1,5):
    print()
    for j in range(1,i+1):
        print(j,end="")

 #Break
 # We can use the break statement with the for loop to terminate the loop when a certain condition is met
 for i in range(5):
    if i == 3:
        break
    print(i,end=" ")  #0 1 2

#continue
#We can use the continue statement with the for loop to skip the current iteration of the loop and jump to the next iteration
for i in range(5):
    if i == 3:
        continue
    print(i,end=" ")  #0 1 2 4 


#Pass
#the pass statement is a null statement which can be used as a placeholder for future code.
#Suppose we have a loop or a function that is not implemented yet, but we want to implement it in the future. In such cases, we can use the pass statement
n = 10
# use pass inside if statement
if n > 10:
    pass






    

       