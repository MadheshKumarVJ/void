#INDEXING

#string indexing
strsample="learning"
print(strsample.index('l'))   #0
print(strsample.index('ning')) #4
print(strsample[7])    #g
print(strsample[-2])   #n

#List indexing
lst=[1,2,'a','hlo',2]
print(lst.index('hlo')) #3
print(lst[2])  #a
print(lst[-1]) #2

#tuple indexing
tup=(1,2,3,4,3,'py')
print(tup.index('py'))  #5
print(tup[2])   #3

#set does not support indexing

#dictionary indexing
dict={1:'first','second':2,3:3,'four':4}
print(dict[1])  #first
print(dict[2])  #keyerror
print(dict['second'])  #2
print(dict['first'])  #keyerror
