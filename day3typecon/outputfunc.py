' ' ' In the below code, After printing good morming! he cursor stays in the same line and prints the next line in the same line since we use end=" " command inside a print()' ' '
print('Good Morning!', end= ' ')
print('It is rainy today')

#object - value(s) to be printed
print('Good Morning!')
# here good morning! is the object which will be printed 

#sep allows us to separate multiple objects inside print(). In the below code comma is seperated with dot
print('New Year', 2023, 'See you soon!', sep= '. ')

#flush is the boolean specifying if the output is flushed or buffered. Default: False
print("Hello, World!", flush=True)


#flush can be well understood from below code 
import time
for i in range(5,0,-1):
    print(i,end='>>',flush=True)
    time.sleep(2) #In the gap of two seconds the values from 5 to 1 will be printed

#File- where the values are printed. It's default value is sys.stdout (screen)
sample = open('samplefile.txt', 'w')
 
print('GeeksForGeeks', file = sample)
sample.close()
#In the above code we can write in the txt file using print()