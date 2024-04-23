#Bitwise AND(&)
a=5 #converts a to binary number
b=4 #converts b to binary number
# performs & operation which has the following rules:
 #1 & 0 = 0
 #0 & 1= 0
 #1 & 1 = 1
 #0 & 0 = 0
print(a&b)  #4

#Bitwise OR(|)
a=5  #converts a to binary number
b=4  #converts b to binary number
# performs | operation which has the following rules:
 #1 | 0 = 1
 #0 | 1= 1
 #1 | 1 = 1
 #0 | 0 = 0
print(a|b)  #5

#Bitwise XOR(^)
a=5   #converts a to binary number
b=4   #converts b to binary number
# performs ^ operation which has the following rules:
 #0, if both bits are same
 #1, if bits are different
print(a^b) #1

#Bitwise NOT(~)
# Whenever we print the compliment of a number, it returns the nagative value of the next suceeding number
# so it will return -6
# To understand this first we will find the complement of 5, then 2's complement of 6, 2's complement is obtained by adding 1 to the frst complement
# The binary value of 2's complement of 6 and complement of 5 will be same
a=5
print(~a)  #-6

#Bitwise left shift(<<)
#In the below code, The first two binary value of 5 from the left side will be discarded, and fills the remaining spaces in right side of binary value with 0
a=5
print(a<<2)  #20

#Bitwise right shift(>>)
#In the below code, The first two binary value of 5 from the right side will be discarded, and fills the remaining spaces in left side of binary value with 0
a=5
print(a>>2)  #1